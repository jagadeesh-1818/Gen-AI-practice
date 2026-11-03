from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv  
load_dotenv()

model = ChatGoogleGenAI(model="gemini-2.5-flash")

result = model.invoke("What's the capital of India?")

print(result.content)
print(langchain_google_genai.__version__)