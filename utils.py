import pdfplumber
import pytesseract
import streamlit as st  # Added Streamlit to access secrets
from PIL import Image
from google import genai
# import os          # No longer needed for the key
# from dotenv import load_dotenv # No longer needed

# load_dotenv() # No longer needed

# Initialize the Client using st.secrets
# Ensure the key name in your Streamlit Cloud dashboard is GEMINI_API_KEY
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_image(image):
    return pytesseract.image_to_string(image)

def explain_clause(clause, language):
    prompt = f"""
    You are a legal expert who explains things to 13-year-olds.
    Translate and explain the following legal clause into {language}.
    
    1. Use very simple words (8th standard level).
    2. Format:
       - **Summary**: 1 sentence summary.
       - **Simple Explanation**: Detailed breakdown.
       - **Why it matters**: Practical impact.
    
    Clause: {clause}
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=prompt
    )
    return response.text