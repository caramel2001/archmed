import streamlit as st
from archmed.pdf import download_pdf, extract_text, preprocess
from archmed.get_wordcloud import generate_wordcloud
from archmed.summarization_and_qna_transformers import *

import matplotlib.pyplot as plt
from st_pages import add_page_title

from streamlit_extras.switch_page_button import switch_page
from archmed.presentationcreator import *
from archmed.slidesoauth import doOauthSlides

PRESENTATION_ID = "1IQUpJg1t2LuCVKL4oN8YRZVj_LjfB9l9NcO5WkI0HfA"


def get_text(pdf):
    with st.spinner("Extracting text....."):
        download_pdf(pdf_url=pdf, dir_path="data", filename="try.pdf")
        text = extract_text(pdf_path="data/try.pdf")
    st.session_state["text"] = text


st.header("Multimodal Content Generation from the Paper")
st.markdown("Using GCP and Google slides to create a automatic presentation")

if st.button("Generate Presentation"):
    if "summary" not in st.session_state.keys():
        st.warning("First Run summary in the Analyse Tab", icon="⚠️")
    service, dservice = doOauthSlides()
    with st.spinner("Creating Presentation....."):
        make_presentation(
            service=service,
            summary_texts=st.session_state["summary"],
            presentation_id=PRESENTATION_ID,
        )

if st.button("Download Presentation"):
    service, dservice = doOauthSlides()
    get_presentation_pdf(
        dservice=dservice,
        presentation_id=PRESENTATION_ID,
        output_file="data/output_2.pdf",
    )
