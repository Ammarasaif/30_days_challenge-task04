from agent import get_gemini_client

def summarize_text(text, use_mcp=False):
    """
    Summarizes the given text using Gemini API.

    Args:
        text: The text to summarize.
        use_mcp: Whether to use Context7 MCP for enhanced context (currently placeholder).

    Returns:
        A string containing the summary.
    """
    model = get_gemini_client()  # Gemini client

    if use_mcp:
        print("Context7 MCP integration placeholder.")

    prompt = f"""
    You are an expert in summarizing educational content. Provide a structured summary with:
    1. Key Concepts (bullet list)
    2. Topic-wise Breakdown
    3. Memory Retention Points (easy bullets)
    4. Detailed Learning Notes (structured bullets)

    Text:
    {text}
    """

    try:
        response = model.generate_content(prompt)  # Gemini's valid method
        return response.text
    except Exception as e:
        return f"An error occurred during summarization: {e}"


