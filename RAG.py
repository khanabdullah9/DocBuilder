from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from huggingface_hub import login
import os

HF_TOKEN = os.getenv("HF_TOKEN")
login(HF_TOKEN)

pdf_dir = os.path.join("uploaded_files")
file = os.listdir(pdf_dir)

pdf_path = os.path.join("uploaded_files",file[0])

loader = PyPDFLoader(pdf_path)
documents = loader.load()
print("PDF LOADED!")

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
chunks = text_splitter.split_documents(documents)
print("DOCUMENT SPLITTED")

embeddings = HuggingFaceEmbeddings(model_name = "BAAI/bge-small-en-v1.5")
print("EMBEDDINGS LOADED")

vector_store = Chroma.from_documents(
    documents = chunks,
    collection_name = file[0].replace(".pdf",""),
    embedding = embeddings,
    persist_directory = "./chroma_langchain_db"
)

print("VECTOR STORE CREATED!")

# while True:
#     user_prompt = input("Prompt (type 'q' to quit):")
#     if user_prompt.strip() == "q":
#         break
#
#     results = vector_store.similarity_search(
#         user_prompt,
#         k = 5
#     )
#
#     for i, doc in enumerate(results, 1):
#         print(f"Result: {i}")
#         print(doc.page_content)
#         print(" ")