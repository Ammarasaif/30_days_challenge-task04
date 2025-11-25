import os
import pandas as pd
from fpdf import FPDF

SAVED_RESULTS_DIR = "saved_results"

def save_text_to_file(filename, content):
    """Saves text content to a file in the saved_results directory."""
    if not os.path.exists(SAVED_RESULTS_DIR):
        os.makedirs(SAVED_RESULTS_DIR)
    with open(os.path.join(SAVED_RESULTS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(content)

def create_pdf(content):
    """Creates a PDF in memory and returns its content as bytes."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add content to the PDF, handling potential encoding issues
    try:
        pdf.multi_cell(0, 10, content)
    except UnicodeEncodeError:
        # Fallback for characters not supported by the default font
        pdf.set_font("Arial", size=12) # Re-set to handle potential state issues
        pdf.multi_cell(0, 10, content.encode('latin-1', 'replace').decode('latin-1'))

    return pdf.output(dest='S').encode('latin-1')


def save_as_csv(filename, data):
    """Saves data (e.g., a list of questions) to a CSV file."""
    if not os.path.exists(SAVED_RESULTS_DIR):
        os.makedirs(SAVED_RESULTS_DIR)
    
    # Assuming data is a list of dictionaries for easy conversion
    df = pd.DataFrame(data)
    df.to_csv(os.path.join(SAVED_RESULTS_DIR, filename), index=False, encoding="utf-8")
