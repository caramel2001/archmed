import re
from string import punctuation
import fitz
import os
import requests
import scipdf
from typing import Optional
import urllib
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
}

exceptions = ["www.ncbi.nlm.nih.gov", "www.sciencedirect.com"]


def preprocess(text: str) -> str:
    # Remove line breaks and extra spaces
    text = text.replace("\n", " ").replace("\r", "")
    text = " ".join(text.split())

    # remove number and sepecial characters
    # text = re.sub("[^A-Za-z]+", " ", text)
    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove special characters
    text = re.sub("[^A-Za-z0-9]+", " ", text)

    # Remove page numbers and headers/footers
    text = re.sub("Page \d+ of \d+", "", text)

    # Remove non-ASCII characters
    text = text.encode("ascii", "ignore").decode()

    # lowercase text
    text = text.lower()

    # remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text


def get_pdf_text(path: str) -> str:
    texts = ""
    # Open the PDF file with PyMuPDF
    with fitz.open(path) as doc:
        for page in doc:
            text = page.get_text()
            texts += text
    return text


def download_pdf(pdf_url: str, dir_path, filename: str):
    # Set the PDF URL and directory path
    # Send a request to the PDF URL and get the response
    if urllib.parse.urlparse(pdf_url).netloc == exceptions:
        get_exception_url(url=pdf_url, exception=urllib.parse.urlparse(pdf_url).netloc)

    print(pdf_url)
    response = requests.get(pdf_url, headers=headers)

    # Create the directory if it doesn't exist
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Save the PDF file to the directory
    pdf_path = os.path.join(dir_path, filename)
    with open(pdf_path, "wb") as f:
        f.write(response.content)


def extract_text(pdf_path) -> Optional[dict]:
    article_dict = scipdf.parse_pdf_to_dict(pdf_path=pdf_path)  # return dictionary
    return article_dict


def get_exception_url(url: str, exception: str):
    if exception == "www.ncbi.nlm.nih.gov":
        page = requests.get(
            f"{pdf_url}/?report=classic",
            headers=headers,
        )
        soup = BeautifulSoup(page.content, "html.parser")

        pdf_url = (
            "https://www.ncbi.nlm.nih.gov"
            + soup.find("li", attrs={"class": "pdf-link other_item"}).find("a")["href"]
        )
    if exception == "www.sciencedirect.com":
        pdf_url = url + "/pdfft"
    return pdf_url
