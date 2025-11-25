import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a given PDF file.

    Args:
        pdf_file: The uploaded PDF file.

    Returns:
        A string containing the extracted text.
    """
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def clean_text(text):
    """
    Cleans the extracted text by removing headers, footers, and extra blank lines.

    Args:
        text: The text to clean.

    Returns:
        A cleaned string.
    """
    # This is a basic cleaning function. It can be improved with more sophisticated logic.
    # Remove page numbers (assuming they are at the start or end of a line)
    text = re.sub(r'^\d+\s|\s\d+$', '', text, flags=re.MULTILINE)
    # Remove headers and footers (simple example, might need more specific patterns)
    text = re.sub(r'(Page \d+ of \d+)', '', text)
    # Replace multiple newlines with a single one
    text = re.sub(r'\n{2,}', '\n', text)
    # Remove leading/trailing whitespace from each line
    text = "\n".join([line.strip() for line in text.split('\n')])
    return text
