import streamlit as st
import os
from dotenv import load_dotenv
from pdf_to_text import load_and_split_pdf, load_multiple_pdfs
from embedded import generate_retriver
from langchain.chains import RetrievalQA
from custom_prompt import custom_prompt
from langchain_community.chat_models import ChatCohere

load_dotenv()

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📄 RAG Chatbot for PDFs")
st.markdown("Upload one or more PDFs and ask questions based on their content.")

uploaded_files = st.file_uploader("Upload PDF(s)", type="pdf", accept_multiple_files=True)

if uploaded_files:
    pdf_names = [file.name for file in uploaded_files]
    pdf_choice = st.selectbox("Select a PDF (or choose 'All PDFs'):", ["All PDFs"] + pdf_names)

    os.makedirs("data", exist_ok=True)
    saved_paths = []
    for file in uploaded_files:
        file_path = os.path.join("data", file.name)
        with open(file_path, "wb") as f:
            f.write(file.read())
        saved_paths.append(file_path)

    st.info(f"Using {'all uploaded PDFs' if pdf_choice == 'All PDFs' else pdf_choice} for answering.")


    if pdf_choice == "All PDFs":
        text_chunks = load_multiple_pdfs(saved_paths)
    else:
        selected_path = os.path.join("data", pdf_choice)
        text_chunks = load_and_split_pdf(selected_path)

   
    retriever = generate_retriver(text_chunks, k=20)

    
    llm = ChatCohere(cohere_api_key=os.getenv("COHERE_API_KEY"), temperature=0.3)


    def safe_get_generation_info(response):
        return {} 
    llm._get_generation_info = safe_get_generation_info

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": custom_prompt}
    )

    question = st.text_input("Ask a question about the selected PDF(s):")
    if question:
        with st.spinner("Thinking..."):
            response = qa_chain.run(question)
        st.success(response)
