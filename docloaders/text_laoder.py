from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv
from pathlib import Path
import os

# Locate project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env from project root
load_dotenv(BASE_DIR / ".env")

print("API KEY LOADED:", os.getenv("GOOGLE_API_KEY") is not None)
model = ChatGoogleGenerativeAI(model= "gemini-3.7-flash")

parser = StrOutputParser()

loader = TextLoader('rag_text.txt')

prompt = PromptTemplate(template= 'Write a summary for the following text -\n {text}',
                        input_variables= ['text'])
docs = loader.load()


chain  = prompt | model | parser

print(chain.invoke({'text' : docs[0].page_content}))

