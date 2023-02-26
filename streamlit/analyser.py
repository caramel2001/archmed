import streamlit as st
from archmed.pdf import download_pdf, extract_text, preprocess
from archmed.get_wordcloud import generate_wordcloud
from archmed.summarization_and_qna_transformers import *

import matplotlib.pyplot as plt
from st_pages import add_page_title

from streamlit_extras.switch_page_button import switch_page


def get_text(pdf):
    with st.spinner("Extracting text....."):
        download_pdf(pdf_url=pdf, dir_path="data", filename="temp.pdf")
        text = extract_text(pdf_path="data/try.pdf")
    st.session_state["text"] = text


add_page_title()
if st.button("Extract Text"):
    get_text(pdf=st.session_state["pdf_url"])

st.header("Summarizer")


if st.button("Summarize Paper"):
    if "text" not in st.session_state.keys():
        get_text(pdf=st.session_state["pdf_url"])
    for i in st.session_state["text"]["sections"]:
        st.markdown(f"### {i['heading']}")
        text = preprocess(i["text"])
        with st.spinner("Generating Summary....."):
            summary = getSummary(
                intro_txt=text, dir="/Users/pratham/Desktop/Ntution/models"
            )
        st.text_area(label="Summary for the Section", value=summary, height=200)
# if "text" in st.session_state.keys():
#     st.write(st.session_state["text"])
