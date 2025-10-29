# tools/pdf_tool.py
import requests, io
from pdfminer.high_level import extract_text
from urllib.parse import urlparse

def download_pdf_text(url, timeout=15):
    resp = requests.get(url, timeout=timeout, stream=True)
    resp.raise_for_status()
    content_type = resp.headers.get("content-type","")
    if "application/pdf" not in content_type and not url.lower().endswith(".pdf"):
        raise ValueError("URL is not a PDF")
    # Save bytes into memory
    bio = io.BytesIO(resp.content)
    text = extract_text(bio)
    return text

from crewai_tools import Tool
pdf_tool = Tool(
    name="PDF Extractor",
    description="Downloads a PDF and returns extracted text",
    func=download_pdf_text
)
