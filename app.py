import streamlit as st
import re

# ---------------------------
# APP CONFIG
# ---------------------------
st.set_page_config(
    page_title="Accounting Equation Solver",
    page_icon="📘",
    layout="wide"
)

# ---------------------------
# LOAD THEORY NOTES
# ---------------------------
@st.cache_data
def load_notes():
    with open("accounting_equation_knowledge.md", "r", encoding="utf-8") as f:
        return f.read()

def split_sections(text):
    sections = []
    current = []
    for line in text.splitlines():
        if line.strip().startswith("#"):
            if current:
                sections.append("\n".join(current))
                current = []
        current.append(line)
    if current:
        sections.append("\n".join(current))
    return sections

# ---------------------------
# LOAD TRANSACTION RULES
# ---------------------------
@st.cache_data
def load_transaction_rules():
    with open("transaction_rules.md", "r", encoding="utf-8") as f:
        return f.read()

def parse_rules(md_text):
    rules = []
    blocks = md_text.split("\n---\n")

    for block in blocks:
        block_lower = block.lower()

        kw_match = re.search(r"\*\*keywords:\*\*(.+)", block_lower)
        journal_match = re.search(r"\*\*journal:\*\*(.+)", block, re.DOTALL)
        effect_match = re.search(r"\*\*effect:\*\*(.+)", block)

        if not kw_match or not journal_match:
            continue

        keywords = [k.strip() for k in kw_match.group(1).split(",")]

        rules.append({
            "keywords": keywords,
            "effect": effect_match.group(1).strip() if effect_match else "",
            "journal": journal_match.group(1).strip()
        })

    return rules

# ---------------------------
# BASIC THEORY SEARCH (ONLY WHEN NO AMOUNT)
# ---------------------------
def search_theory(question, sections):
    q_words = set(question.lower().split())
    scored = []

    for sec in sections:
        score = len(q_words & set(sec.lower().split()))
        if score > 0:
            scored.append((score, sec))

    scored.sort(reverse=True)
    return scored[0][1] if scored else None

# ---------------------------
# AMOUNT EXTRACTION
# ---------------------------
def extract_amount(text):
    match = re.search(r"₹?\s?(\d+)", text.replace(",", ""))
    return int(match.group(1)) if match else None

# ---------------------------
# RULE-BASED SOLVER (FIXED)
# ---------------------------
def solve_transaction(question, rules):
    q = question.lower()
    amount = extract_amount(q)

    if not amount:
        return None, "NO_AMOUNT"

    for rule in rules:
        # ✅ FIX: match ANY keyword, not ALL
        if any(k in q for k in rule["keywords"]):
            return format_answer(
                transaction=question.strip().capitalize(),
                amount=amount,
                effect=rule["effect"],
                journal=rule["journal"]
            ), "SOLVED"

    return None, "NO_RULE"

# ---------------------------
# OUTPUT TEMPLATE
# ---------------------------
def format_answer(transaction, amount, effect, journal):
    return f"""
### Transaction
{transaction}

### Accounting Equation
Assets = Liabilities + Capital

### Effect
{effect.replace("₹", f"₹{amount}")}

### Equation Treatment
Effect applied using amount ₹{amount}

### Journal Entry
{journal.replace("₹", f"₹{amount}")}
"""

# ---------------------------
# UI
# ---------------------------
def main():
    st.title("📘 Accounting Equation Solver")
    st.caption("Rule-based accounting engine using Markdown (No AI, No API)")

    notes = load_notes()
    sections = split_sections(notes)

    rules_md = load_transaction_rules()
    rules = parse_rules(rules_md)

    question = st.text_input(
        "Ask a question",
        placeholder="Example: Purchase of land and building worth 2000000"
    )

    if st.button("Get Answer", use_container_width=True):
        if not question.strip():
            st.warning("Please enter a question.")
            return

        answer, status = solve_transaction(question, rules)

        if status == "SOLVED":
            st.markdown(answer)

        elif status == "NO_AMOUNT":
            theory = search_theory(question, sections)
            if theory:
                st.markdown("### Explanation")
                st.markdown(theory)
            else:
                st.error("This information is not available in the provided notes.")

        else:
            st.error(
                "This transaction type is not yet defined in transaction_rules.md."
            )

if __name__ == "__main__":
    main()

