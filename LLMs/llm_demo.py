from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini")

result = llm.invoke("What is the capital of India?")

print(result.content)
