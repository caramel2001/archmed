import streamlit as st
from archmed.pdf import download_pdf, extract_text
from streamlit_extras.switch_page_button import switch_page


def get_text(pdf):
    with st.spinner("Extracting text....."):
        download_pdf(pdf_url=pdf, dir_path="data", filename="try.pdf")
        text = extract_text(pdf_path="data/try.pdf")
        return text


text = get_text(pdf=st.session_state["pdf_url"])
st.write(text)
