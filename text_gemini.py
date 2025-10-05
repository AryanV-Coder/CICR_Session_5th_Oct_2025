import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

prompt = input("PROMPT : ")

final_prompt =[
            {
                "role": "user",
                "parts": [
                    {
                        "text": "You are a famous musician. Always answer any user query in a rhyming style."
                    }
                ]
            },
            {
                "role": "user",
                "parts": [
                    {
                        "text": f"{prompt}"
                    }
                ]
            }
        ]

response = model.generate_content(final_prompt)
print(response.text)