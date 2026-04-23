import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyBTvQ4fuY79yEheXVHYfsKcT58Chwm09x8")
model = genai.GenerativeModel("gemini-3.1-flash-lite-preview")
chat = model.start_chat(history=[])

print("vidhya sati Chatbot(Type 'exist' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exist","quit","bye"]:
        break
    response = chat.send_message(user_input)
    print(f"vidhya sati:{response.text}")
