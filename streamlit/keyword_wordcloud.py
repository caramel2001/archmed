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


st.header("Biomedical Keyword extraction")
st.markdown(
    "Using spaCy en_core_sci_md entities to perform keyword extraction and wordcloud generation"
)
if st.button("Generate WordCloud"):
    if "text" not in st.session_state.keys():
        get_text(pdf=st.session_state["pdf_url"])
    with st.spinner("Generating Wordcloud....."):
        wc = generate_wordcloud(st.session_state["text"]["abstract"], bg_color="black")
    fig = plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wc)
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(fig)
