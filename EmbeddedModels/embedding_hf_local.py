from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

doc = ["The capital of India is New Delhi.", 
       "The capital of France is Paris.", 
       "The capital of Germany is Berlin.",
       "The capital of Italy is Rome."]

result = embeddings.embed_documents(doc)

print(str(result))
