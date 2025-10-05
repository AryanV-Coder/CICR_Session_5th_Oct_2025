import google.generativeai as genai
import base64
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

with open("video1.mp4", "rb") as file:
    contents = file.read()

encoded_video = base64.b64encode(contents).decode('utf-8')

prompt = [  
            {
                "role": "user",
                "parts": [
                    {
                        "text": "What can you see in this video. Analyse in detail. Answer in 4 lines."
                    }
                ]
            },
            {
                "role": "user",
                "parts": [
                    {
                        "mime_type": "video/mp4",
                        "data": encoded_video
                    }
                ]
            }
        ]

response = model.generate_content(prompt)
print(response.text)
