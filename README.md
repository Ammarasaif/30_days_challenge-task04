# PDF Notes Summarizer & Quiz Generator

This web application allows users to upload PDF notes, extract content, summarize key concepts, and automatically generate quizzes.

## Features

- **PDF Upload & Extraction**: Upload PDF files up to 50MB.
- **AI-Powered Summarization**: Generate summaries of your notes.
- **Automatic Quiz Generation**: Create quizzes with multiple-choice, true/false, and short answer questions.
- **Download Results**: Download summaries and quizzes in TXT and PDF formats.

## Tech Stack

- **Backend**: Python
- **UI**: Streamlit
- **PDF Handling**: PyMuPDF
- **AI**: OpenAI

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd pdf-notes-quiz-app
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file** in the root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your_openai_api_key"
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

5.  Open your browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

## File Structure

```
pdf-notes-quiz-app/
│── app.py                    # Streamlit Main UI
│── agent.py                  # OpenAI Agents SDK + Gemini logic
│── pdf_reader.py             # PyPDF extraction & cleaning
│── quiz_generator.py         # Quiz creation logic
│── summarizer.py             # AI summarization module
│── utils.py                  # Helper functions
│── requirements.txt          # Dependencies
│── README.md                 # Guide & instructions
│── /saved_results            # Store summaries & quizzes
│── /context_mcp              # MCP memory context storage
│── gemini.md                 # Instruction file
```
