import streamlit as st
import sys
from pathlib import Path

sys.path.append("/Users/pratham/Desktop/Ntution")
import webbrowser
import urllib
import base64
from typing import List
from st_pages import Page, show_pages, add_page_title
from archmed.search import get_search
from streamlit_extras.switch_page_button import switch_page

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page(
            "/Users/pratham/Desktop/Ntution/streamlit/researchworkspaceui.py",
            "Research Workspace",
            "🕵️",
        ),
        Page("streamlit/chatbotpage.py", "ArchMed ChatBot", "🤖"),
        Page("streamlit/analyser.py", "Summerizer", "✍️s"),
    ]
)

# Optional -- adds the title and icon to the current page
add_page_title()


quer = st.text_input("search")
result = get_search(quer)


def callback(pdf):
    switch_page("Summerizer")


for i, res in enumerate(result):
    if "eprint_url" in res.keys():
        col1, col2 = st.columns(2)

        with col1:
            if res["eprint_url"]:
                html_string = f"<h5>{res['bib']['title']}</h5>"

                st.markdown(html_string, unsafe_allow_html=True)

                html_string = f"<h8>{res['bib']['author']}</h8>"
                st.markdown(html_string, unsafe_allow_html=True)
                html_string = f"<h7> <u>Publication Year</u>:</h7><h8>{res['bib']['pub_year']}</h8>"
                st.markdown(html_string, unsafe_allow_html=True)

                html_string = f"<div><h7> <u>Numver of Citations</u>:</h7><h8>{res['num_citations']}</h8><div>"
                st.markdown(html_string, unsafe_allow_html=True)
            # st.markdown("---")
            else:
                continue

        with col2:
            if res["eprint_url"]:
                html_string = f"<a href={res['eprint_url']}>Go to paper</a>"
                st.markdown(html_string, unsafe_allow_html=True)

                html_string = f"<h5>{res['bib']['abstract']}</h5>"
                st.markdown(html_string, unsafe_allow_html=True)
            # st.markdown("---")
            else:
                continue
        if st.button(label=f"Analyse", key=i, kwargs={"pdf": res["eprint_url"]}):
            st.session_state["pdf_url"] = res["eprint_url"]
            switch_page("Summerizer")

        st.markdown("---")

    else:
        continue


# function to display the PDF of a given file
col1, col2 = st.columns(2)


def displayPDF(file):
    # Opening file from file path. this is used to open the file from a website rather than local
    with urllib.request.urlopen(file) as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    # Embedding PDF in HTML
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


display = False
with col1:
    url = st.text_input("The URL link")
with col2:
    st.write(" ")
    st.write(" ")
    if st.button("import pdf") and url is not None:
        display = True
if display == True:
    displayPDF(f"{url}")

url = "https://docs.google.com/presentation/d/1EW8JearggoLRPXN6qiPvHPujHsrVANaHTgPBlgf2cmE/edit#slide=id.SLIDES_API1686381278_0"
if st.button("Generate Presentation"):
    webbrowser.open_new_tab(url)
