import easyocr
import streamlit as st


@st.cache_resource
def get_ocr_reader():
    reader = easyocr.Reader(['en'])
    return reader
