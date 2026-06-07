import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_repository_report(repo_data, languages, readme):

    response = model.generate_content(
        "Explain React in one short paragraph."
    )

    return response.text