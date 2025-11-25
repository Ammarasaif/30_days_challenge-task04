import streamlit as st
import os

from pdf_reader import extract_text_from_pdf, clean_text
from summarizer import summarize_text
from quiz_generator import generate_quiz
from utils import save_text_to_file, create_pdf

# --- Page Config with Dark Mode ---
st.set_page_config(
    page_title="PDF Notes Summarizer & Quiz Generator",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Stylish Fonts and Dark Mode ---
st.markdown(
    """
    <style>
    /* Dark Mode Background & Font Colors */
    body, .stApp, .css-1v3fvcr, .css-18e3th9 {
        background-color: #0E1117;
        color: #F5F5F5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background-color: #1C1F26;
        padding: 20px;
        border-radius: 10px;
    }

    /* TextArea Styling */
    textarea, .stTextArea textarea {
        background-color: #1C1F26;
        color: #F5F5F5;
        border: 1px solid #555;
        border-radius: 5px;
        font-size: 14px;
    }

    /* Buttons Styling */
    .stButton>button {
        background-color: #4ECCA3;
        color: #0E1117;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1.5em;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3ba77b;
        color: white;
        cursor: pointer;
    }

    /* Tabs Styling */
    .css-1ynaq5j {
        background-color: #1C1F26;
        border-radius: 10px;
        padding: 10px;
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #FFD369;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- App Title ---
st.markdown("<h1 style='text-align:center;'>📝 PDF Notes Summarizer & Quiz Generator</h1>", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.header("Upload your PDF 📂")
    uploaded_file = st.file_uploader(
        "Choose a PDF file (max 50MB)",
        type="pdf",
        accept_multiple_files=False,
    )
    st.info("This app helps you summarize your PDF notes and generate quizzes from them.")
   

# --- Main Content ---
if uploaded_file is not None:
    if uploaded_file.size > 50 * 1024 * 1024:
        st.error("File size exceeds 50MB. Please upload a smaller file.")
    else:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

        with st.spinner("Processing PDF..."):
            extracted_text = extract_text_from_pdf(uploaded_file)
            cleaned_text = clean_text(extracted_text)

        st.header("Extracted Text")
        st.text_area("Cleaned Text", cleaned_text, height=250)

        # --- Actions ---
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Generate Summary 📝"):
                with st.spinner("Generating summary..."):
                    summary = summarize_text(cleaned_text)
                    st.session_state['summary'] = summary

        with col2:
            if st.button("Generate Quiz ❓"):
                with st.spinner("Generating quiz..."):
                    quiz = generate_quiz(cleaned_text)
                    st.session_state['quiz'] = quiz

        # --- Tabs for Results ---
        tab1, tab2 = st.tabs(["Summary", "Quiz"])

        with tab1:
            if 'summary' in st.session_state:
                st.subheader("Summary")
                st.markdown(st.session_state['summary'])

                # --- Download Summary ---
                st.download_button(
                    label="Download Summary as TXT",
                    data=st.session_state['summary'],
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}_summary.txt",
                    mime="text/plain"
                )
                st.download_button(
                    label="Download Summary as PDF",
                    data=create_pdf(st.session_state['summary']),
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}_summary.pdf",
                    mime="application/pdf"
                )

        with tab2:
            if 'quiz' in st.session_state:
                st.subheader("Quiz")
                st.markdown(st.session_state['quiz'])

                # --- Download Quiz ---
                st.download_button(
                    label="Download Quiz as TXT",
                    data=st.session_state['quiz'],
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}_quiz.txt",
                    mime="text/plain"
                )
                st.download_button(
                    label="Download Quiz as PDF",
                    data=create_pdf(st.session_state['quiz']),
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}_quiz.pdf",
                    mime="application/pdf"
                )
else:
    st.info("Please upload a PDF file to get started.")


# def main():
#     print("Hello from pdf-quiz-app!")


# if __name__ == "__main__":
#     main()
