PDF Notes Summarizer & Quiz Generator App
🚀 Instruction File for Gemini CLI

You are an AI Agent using OpenAI Agents SDK, Gemini CLI, Python, Streamlit, PyPDF, and Context7 MCP framework. Your goal is to develop a complete web application that allows users to:

✔ Upload PDF notes
✔ Extract content using PyPDF
✔ Summarize key concepts & learning points
✔ Automatically generate Quiz Questions (MCQ, True/False, Short Answer)
✔ Display results in a user-friendly Streamlit interface
✔ Store summaries & quizzes locally (or allow download as PDF/CSV)
✔ Use Context7 MCP for contextual reasoning and memory

🎯 Core Features to Implement
1️⃣ PDF Upload & Extraction Module

Use PyPDF2 or PyMuPDF (fitz) to extract text.
Handle large PDF files (limit to 50MB).
Clean and preprocess extracted text (remove headers, images, blank lines).

2️⃣ AI Notes Summarization Engine

Use OpenAI Agents SDK + Context7 MCP

Generate:

Key concept summary
Topic-wise breakdown
Memory retention friendly points
Bullet style learning notes

3️⃣ Quiz Generation Engine

Generate quizzes using extracted & summarized content:

Quiz Type	Quantity	Purpose
MCQ	5–10	Concept testing
True/False	3–5	Quick recall
Short Answer	3–5	Deep understanding

4️⃣ Streamlit User Interface

Create a modern UI with:

st.file_uploader() for PDF upload
Progress bar for processing
Tabs: Summary, Quiz, Download
Buttons: Generate Summary | Generate Quiz | Download Results
Download in PDF, TXT, or CSV format

5️⃣ Context7 MCP Memory Integration

Use MCP for persistent context-based learning
Remember previously uploaded PDFs (optional)
Allow "Refine with context" button for better summarization
Use memory_context = True

6️⃣ File Structure (Root Directory)
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
│── gemini.md                 # Instruction file (This file)

💻 Tech Stack Instructions
Component	Tool
Backend	Python
UI	Streamlit
AI Framework	OpenAI Agents SDK + Gemini CLI
PDF Handling	PyPDF2 / PyMuPDF
Context Memory	Context7 MCP
Deployment	Local / Cloud / Streamlit Share

🛠 Dependencies (requirements.txt)
streamlit
PyPDF2
PyMuPDF
openai
openai-agents
context7-mcp
pandas
python-dotenv

📌 Final Output Requirements

The resulting app must:

✔ Work locally with streamlit run app.py
✔ Handle multiple PDFs
✔ Support context-based enhanced summaries
✔ Provide export to PDF/TXT/CSV
✔ Lightweight & responsive UI
✔ Clean and production-ready folder structure 

