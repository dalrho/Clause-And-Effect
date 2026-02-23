from google import genai
from app.core.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def call_llm(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config={
            "system_instruction": "You are a legal contract analyzer. Return strictly valid JSON.",
            "temperature": 0.1,
            "response_mime_type": "application/json", # <--- This is key
        },
        contents=prompt
    )
    return response.text