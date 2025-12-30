import streamlit as st
from utils import extract_text_from_pdf, extract_text_from_image, explain_clause
from PIL import Image

st.set_page_config(page_title="Contract Explainer", page_icon="⚖️")
st.title("⚖️ Contract Clause Explainer")
st.write("Upload a contract and get explanations in simple language.")

uploaded_file = st.file_uploader(
    "Upload PDF or Image", type=["pdf", "jpg", "jpeg", "png"]
)

if uploaded_file:
    with st.spinner("Extracting text..."):
        if uploaded_file.type == "application/pdf":
            # Save temp file to read
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            full_text = extract_text_from_pdf("temp.pdf")
        else:
            image = Image.open(uploaded_file)
            full_text = extract_text_from_image(image)

    st.subheader("1. Extracted Text")
    st.info("Copy the specific clause you want to understand from below.")
    text_area = st.text_area("Full Document Text", full_text, height=250)

    st.divider()

    st.subheader("2. Explain Clause")
    selected_clause = st.text_area("Paste the clause here:")

    col1, col2 = st.columns(2)
    with col1:
        lang = st.selectbox(
            "Target Language", ["English", "Hindi", "Marathi", "Spanish", "French"]
        )
    with col2:
        custom_lang = st.text_input("Or type any other language:")

    final_lang = custom_lang if custom_lang else lang

    if st.button("Explain Now ✨"):
        if selected_clause:
            explanation = explain_clause(selected_clause, final_lang)
            st.success(f"Explanation in {final_lang}:")
            st.markdown(explanation)
        else:
            st.warning("Please paste a clause first!")
