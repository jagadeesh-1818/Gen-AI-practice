
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env from the project root
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.7
)

# Print the response
response = model.invoke(
    "explain about W11 mercedes in detail"
)

print(response.text)
