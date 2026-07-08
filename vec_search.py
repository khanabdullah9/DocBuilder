from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from huggingface_hub import login
from dotenv import load_dotenv
import os

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")
login(HF_TOKEN)

embeddings = HuggingFaceEmbeddings(model_name = "BAAI/bge-small-en-v1.5")

vector_store = Chroma(
    collection_name="Agentic_AI_300_Words",
    persist_directory = "./chroma_langchain_db",
    embedding_function = embeddings,
)

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