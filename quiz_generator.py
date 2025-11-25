from agent import get_gemini_client

def generate_quiz(text):
    """
    Generates a quiz based on the provided text using Gemini API.

    Args:
        text: The text to base the quiz on.

    Returns:
        A string containing the quiz questions.
    """
    model = get_gemini_client()  # Gemini client

    prompt = f"""
    You are an expert quiz creator for educational purposes. Based on the following text, generate a quiz with:
    - 5-10 Multiple Choice Questions (MCQs) with correct answers
    - 3-5 True/False Questions
    - 3-5 Short Answer Questions

    The quiz should test understanding of key concepts.

    Text:
    {text}
    """

    try:
        response = model.generate_content(prompt)  # ✅ Gemini API method
        return response.text  # ✅ Correct attribute
    except Exception as e:
        return f"An error occurred during quiz generation: {e}"
