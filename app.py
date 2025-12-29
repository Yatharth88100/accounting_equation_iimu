import streamlit as st

# ---------------------------
# APP CONFIG
# ---------------------------
st.set_page_config(
    page_title="Accounting Equation Knowledge App",
    page_icon="📘",
    layout="wide"
)

# ---------------------------
# LOAD MARKDOWN NOTES
# ---------------------------
@st.cache_data
def load_notes():
    with open("accounting_equation_knowledge.md", "r", encoding="utf-8") as f:
        return f.read()

def split_into_sections(text):
    sections = []
    current = []

    for line in text.splitlines():
        if line.strip().startswith("#"):
            if current:
                sections.append("\n".join(current).strip())
                current = []
        current.append(line)

    if current:
        sections.append("\n".join(current).strip())

    return sections

# ---------------------------
# SEARCH LOGIC (NO AI)
# ---------------------------
def find_relevant_sections(question, sections, top_k=3):
    q_words = set(question.lower().split())
    scored = []

    for sec in sections:
        sec_words = set(sec.lower().split())
        score = len(q_words & sec_words)
        if score > 0:
            scored.append((score, sec))

    scored.sort(reverse=True)
    return [sec for _, sec in scored[:top_k]]

# ---------------------------
# UI
# ---------------------------
def main():
    st.title("📘 Accounting Equation – Knowledge Explorer")
    st.caption("Notes-based learning system (No AI, No API)")

    st.info(
        "This tool answers questions strictly from the provided accounting notes. "
        "If the information is not present, it will clearly say so."
    )

    notes_text = load_notes()
    sections = split_into_sections(notes_text)

    st.success("Accounting notes loaded successfully")

    question = st.text_input(
        "Ask a question",
        placeholder="Example: Why does income increase capital?"
    )

    if st.button("Search Answer", use_container_width=True):
        if not question.strip():
            st.warning("Please enter a question.")
            return

        results = find_relevant_sections(question, sections)

        if not results:
            st.error("This information is not available in the provided notes.")
        else:
            st.subheader("📖 Relevant Explanation")
            for i, res in enumerate(results, start=1):
                st.markdown(f"### Result {i}")
                st.markdown(res)
                st.markdown("---")

if __name__ == "__main__":
    main()
