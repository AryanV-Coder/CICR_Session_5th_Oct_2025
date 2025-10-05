import google.generativeai as genai
import base64
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

with open("img1.png", "rb") as file:
    contents = file.read()

encoded_image = base64.b64encode(contents).decode('utf-8')

prompt = [  
            {
                "role": "user",
                "parts": [
                    {
                        "text": "Comment on this image in only 4 lines : "
                    }
                ]
            },
            {
                "role": "user",
                "parts": [
                    {
                        "mime_type": "image/png",
                        "data": encoded_image
                    }
                ]
            }
        ]

response = model.generate_content(prompt)
print(response.text)
