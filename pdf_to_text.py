from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def load_and_split_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    for doc in documents:
        doc.metadata["source"] = os.path.basename(file_path)

    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    return splitter.split_documents(documents)


def load_multiple_pdfs(file_paths):
    all_documents = []
    for path in file_paths:
        loader = PyPDFLoader(path)
        docs = loader.load()
        for doc in docs:
            # ✅ This sets correct file name as metadata
            doc.metadata["source"] = os.path.basename(path)
        all_documents.extend(docs)

    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    return splitter.split_documents(all_documents)

