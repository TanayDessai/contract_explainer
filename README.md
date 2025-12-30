# ⚖️ Contract Clause Explainer

A Generative AI-powered tool designed to bridge the gap between complex legal jargon and plain English. This application allows users to upload contract documents (PDFs or Images), extract text via OCR, and receive simple, 8th-grade level explanations of specific clauses in multiple languages.

---

## 🌟 Features

* **Multimodal Input:** Supports both digital PDFs and scanned images/photos of documents.
* **AI-Powered Simplification:** Converts dense "Legalese" into clear, understandable language for non-lawyers.
* **Multilingual Support:** Get explanations in **English, Hindi, Marathi**, or any other language of your choice.
* **8th-Grade Level Logic:** Specifically tuned to explain complex legal obligations as if speaking to a 13-year-old.
* **Modern Tech Stack:** Built with the 2025 Google Gen AI SDK and Streamlit for a fast, responsive UI.

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **AI Model:** Gemini 2.5 Flash (via `google-genai`)
* **Frontend:** Streamlit
* **OCR & Extraction:** `pdfplumber` (PDFs) and `pytesseract` (Images)
* **Environment:** `python-dotenv`

---

## 🚀 Getting Started

### 1. Prerequisites
* **Python:** Install Python 3.10 or higher.
* **Tesseract OCR:** Required for image-to-text functionality.
    * **Windows:** [Download Installer](https://github.com/UB-Mannheim/tesseract/wiki) (Add to System PATH).
    * **Mac:** `brew install tesseract`
    * **Linux:** `sudo apt install tesseract-ocr`

### 2. Installation
Clone this repository or create your project folder, then set up a virtual environment:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt