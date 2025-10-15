from google import genai
from dotenv import load_dotenv

from .config import settings


load_dotenv()

client = genai.Client(api_key=settings.GEMINI_API_KEY)

def ask_gemini(contents: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=contents
        )
    except Exception as e:
        raise e

    return response.text
