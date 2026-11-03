from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

doc = ["The capital of India is New Delhi.", 
       "The capital of France is Paris.", 
       "The capital of Germany is Berlin.",
       "The capital of Italy is Rome."]

query = "tell me about India"

doc_embeddings = embedding.embed_documents(doc)
query_embeddings = embedding.embed_query(query)


scores = cosine_similarity([query_embeddings], doc_embeddings)

print(scores)