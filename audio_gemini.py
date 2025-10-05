import google.generativeai as genai
import base64
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

with open("audio1.wav", "rb") as file:
    contents = file.read()

encoded_audio = base64.b64encode(contents).decode('utf-8')

prompt = [  
            {
                "role": "user",
                "parts": [
                    {
                        "text": "Give me Transcript and Meaning of this audio file."
                    }
                ]
            },
            {
                "role": "user",
                "parts": [
                    {
                        "mime_type": "audio/wav",
                        "data": encoded_audio
                    }
                ]
            }
        ]

response = model.generate_content(prompt)
print(response.text)
