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
# LOAD NOTES
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
# BASIC SEARCH (THEORY)
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
# NUMERICAL LOGIC
# ---------------------------
def extract_amount(text):
    match = re.search(r"₹?\s?(\d+)", text.replace(",", ""))
    return int(match.group(1)) if match else None

def solve_transaction(question):
    q = question.lower()
    amount = extract_amount(q)

    if not amount:
        return None

    # RENT
    if "rent" in q and "paid" in q:
        return format_answer(
            transaction=f"Paid rent ₹{amount}",
            debit="Rent A/c",
            credit="Cash A/c",
            amount=amount,
            explanation="because rent is an expense"
        )

    # SALARY
    if "salary" in q and "paid" in q:
        return format_answer(
            transaction=f"Paid salary ₹{amount}",
            debit="Salary A/c",
            credit="Cash A/c",
            amount=amount,
            explanation="because salary is an expense"
        )

    # DEPRECIATION
    if "depreciation" in q:
        return format_answer(
            transaction=f"Depreciation charged ₹{amount}",
            debit="Depreciation A/c",
            credit="Asset A/c",
            amount=amount,
            explanation="because depreciation is a non-cash expense"
        )

    return None

# ---------------------------
# OUTPUT TEMPLATE
# ---------------------------
def format_answer(transaction, debit, credit, amount, explanation):
    return f"""
### Transaction
{transaction}

### Accounting Equation
Assets = Liabilities + Capital

### Effect
- Cash (Asset) ↓ ₹{amount}
- Capital ↓ ₹{amount} ({explanation})

### Equation Treatment
Assets ↓ ₹{amount} = Capital ↓ ₹{amount}

### Journal Entry
- {debit} Dr ₹{amount}
- To {credit} ₹{amount}
"""

# ---------------------------
# UI
# ---------------------------
def main():
    st.title("📘 Accounting Equation Solver")
    st.caption("Notes-based theory + numerical problem solver (No AI, No API)")

    notes = load_notes()
    sections = split_sections(notes)

    question = st.text_input(
        "Ask a question",
        placeholder="Example: I paid a rent for 15570. Accounting equation treatment"
    )

    if st.button("Get Answer", use_container_width=True):
        if not question.strip():
            st.warning("Please enter a question.")
            return

        numerical_answer = solve_transaction(question)

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
