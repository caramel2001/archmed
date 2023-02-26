import streamlit as st
from archmed.pdf import download_pdf, extract_text, preprocess, get_images
from archmed.get_wordcloud import generate_wordcloud
from archmed.summarization_and_qna_transformers import *
import io
import matplotlib.pyplot as plt
from st_pages import add_page_title
import boto3
from utils import settings

from streamlit_extras.switch_page_button import switch_page


def get_text(pdf):
    with st.spinner("Extracting text....."):
        download_pdf(pdf_url=pdf, dir_path="data", filename="temp.pdf")
        text = extract_text(pdf_path="data/temp.pdf")
    st.session_state["text"] = text


add_page_title()
if st.button("Extract Text"):
    get_text(pdf=st.session_state["pdf_url"])

st.header("Summarizer")


if st.button("Summarize Paper"):
    if "text" not in st.session_state.keys():
        get_text(pdf=st.session_state["pdf_url"])
    st.session_state["summary"] = {}
    # images = get_images("data/temp.pdf")
    # print(images)
    curr = 0
    for count, i in enumerate(st.session_state["text"]["sections"]):
        st.markdown(f"### {i['heading']}")
        text = preprocess(i["text"])
        st.session_state["summary"][i["heading"]] = {}
        with st.spinner("Generating Summary....."):
            summary = getSummary(
                intro_txt=text, dir="/Users/pratham/Desktop/Ntution/models"
            )
            # if i["n_figure_ref"] != 0:
            #     for j in range(i["n_figure_ref"]):
            #         if curr == len(images):
            #             st.session_state["summary"][i["heading"]]["images"] = None
            #             break
            #         f = io.BytesIO(images[curr])
            #         client = boto3.client(
            #             "s3",
            #             aws_access_key_id=settings["AWS_ID"],
            #             aws_secret_access_key=settings["AWS_SECRET"],
            #         )
            #         f = io.BytesIO(images[curr])
            #         client.upload_fileobj(
            #             f,
            #             "imagesarchmed",
            #             f"imagesarchmed/{curr}",
            #         )
            #         curr += 1
            #         st.session_state["summary"][i["heading"]][
            #             "images"
            #         ] = "imagesarchmed/{curr}"

            # else:
            st.session_state["summary"][i["heading"]]["images"] = None
            st.session_state["summary"][i["heading"]]["summary"] = summary

        st.text_area(
            label="Summary for the Section", value=summary, key=count, height=200
        )
# if "text" in st.session_state.keys():
#     st.write(st.session_state["text"])
