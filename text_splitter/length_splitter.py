from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\suhas\OneDrive\Desktop\gen ai_campusX\others\Jagadeesh B R_Resume.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap= 0,
    separator= ''
)

result = splitter.split_documents(docs)

print("Total chunks:", len(result))

for i, chunk in enumerate(result):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk.page_content)
    print("Metadata:", chunk.metadata)