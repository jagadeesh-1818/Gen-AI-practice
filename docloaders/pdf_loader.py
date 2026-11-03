from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

loader = PyPDFLoader('C:\Users\suhas\OneDrive\Desktop\gen ai_campusX\others\rag_text.pdf')

docs = loader.load()

print(len(docs))