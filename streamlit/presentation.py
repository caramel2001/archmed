import streamlit as st
from archmed.pdf import download_pdf, extract_text, preprocess
from archmed.get_wordcloud import generate_wordcloud
from archmed.summarization_and_qna_transformers import *

import matplotlib.pyplot as plt
from st_pages import add_page_title

from streamlit_extras.switch_page_button import switch_page


def get_text(pdf):
    with st.spinner("Extracting text....."):
        download_pdf(pdf_url=pdf, dir_path="data", filename="try.pdf")
        text = extract_text(pdf_path="data/try.pdf")
    st.session_state["text"] = text


st.header("Multimodal Content Generation from the Paper")
st.markdown("Using GCP and Google slides to create a automatic presentation")
if st.button("Generate Presentation"):
    if "text" not in st.session_state.keys():
        get_text(pdf=st.session_state["pdf_url"])
    with st.spinner("Generating Wordcloud....."):
        wc = generate_wordcloud(st.session_state["text"]["abstract"], bg_color="black")
