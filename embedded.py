import os
import hashlib
import json
from dotenv import load_dotenv
load_dotenv()

from langchain_community.embeddings import CohereEmbeddings
from langchain_community.vectorstores import FAISS

faiss_path = "faiss_index"
hash_path = "data_hash.json"
data_folder = "data"

os.environ["LANGCHAIN_USER_AGENT"] = "chatbot-using-cohere"


def get_folder_hash(folder_path):
    """Generate a hash based on PDF file names + their sizes"""
    hash_md5 = hashlib.md5()
    for root, _, files in os.walk(folder_path):
        for file in sorted(files):
            if file.endswith(".pdf"):
                path = os.path.join(root, file)
                hash_md5.update(file.encode())
                hash_md5.update(str(os.path.getsize(path)).encode())
    return hash_md5.hexdigest()

def load_or_create_index(text_chunks):
    embeddings = CohereEmbeddings(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    user_agent="chatbot-using-cohere"
)


    current_hash = get_folder_hash(data_folder)

    if os.path.exists(faiss_path) and os.path.exists(hash_path):
        with open(hash_path, "r") as f:
            saved_hash = json.load(f).get("hash")
        if saved_hash == current_hash:
            print("📦 Using cached FAISS index.")
            return FAISS.load_local(faiss_path, embeddings, allow_dangerous_deserialization=True)


    print("📄 PDFs changed. Rebuilding FAISS index...")
    vector_store = FAISS.from_documents(text_chunks, embeddings)
    vector_store.save_local(faiss_path)

    with open(hash_path, "w") as f:
        json.dump({"hash": current_hash}, f)

    return vector_store


def generate_retriver(text_chunks, k=20):
    vector_store = load_or_create_index(text_chunks)
    return vector_store.as_retriever(search_kwargs={"k": k})
