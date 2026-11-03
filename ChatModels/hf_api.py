from dotenv import load_dotenv
from pathlib import Path
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=True)

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)