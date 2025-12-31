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
        if "**Keywords:**" in block:
            rules.append(block)
    return rules

# ---------------------------
# BASIC THEORY SEARCH
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
# NUMERICAL HELPERS
# ---------------------------
def extract_amount(text):
    match = re.search(r"₹?\s?(\d+)", text.replace(",", ""))
    return int(match.group(1)) if match else None

# ---------------------------
# RULE-BASED SOLVER
# ---------------------------
def solve_transaction(question, rules):
    q = question.lower()
    amount = extract_amount(q)

    if not amount:
        return None

    for rule in rules:
        keyword_line = re.search(r"\*\*Keywords:\*\*(.*)", rule)
        if not keyword_line:
            continue

        keywords = [k.strip().lower() for k in keyword_line.group(1).split(",")]

        if all(k in q for k in keywords):
            return format_answer(rule, amount)

    return None

# ---------------------------
# OUTPUT TEMPLATE
# ---------------------------
def format_answer(rule_text, amount):
    return f"""
### Transaction
{rule_text}

### Amount Used
₹{amount}

### Note
This solution is generated dynamically using rule-based accounting logic.
"""

# ---------------------------
# UI
# ---------------------------
def main():
    st.title("📘 Accounting Equation Solver")
    st.caption("Rule-based accounting system using Markdown (No AI, No API)")

    notes = load_notes()
    sections = split_sections(notes)

    rule_text = load_transaction_rules()
    rules = parse_rules(rule_text)

    question = st.text_input(
        "Ask a question",
        placeholder="Example: Accounting equation for purchase of land and building of 2000000"
    )

    if st.button("Get Answer", use_container_width=True):
        if not question.strip():
            st.warning("Please enter a question.")
            return

        numerical_answer = solve_transaction(question, rules)

        if numerical_answer:
            st.markdown(numerical_answer)
        else:
            theory = search_theory(question, sections)
            if theory:
                st.markdown("### Explanation")
                st.markdown(theory)
            else:
                st.error("This information is not available in the provided notes.")

if __name__ == "__main__":
    main()
