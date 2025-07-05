# pdf-rag-chatbot
An AI-powered chatbot that answers questions from uploaded PDF documents using Retrieval-Augmented Generation (RAG). Built with Streamlit, LangChain, Cohere, and FAISS.
# 📄 PDF RAG Chatbot

This project is an AI-powered chatbot that answers natural language questions from uploaded PDF files. It uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers directly from the document contents.

## 🚀 Features

- Upload one or multiple PDFs
- Ask questions in natural language
- Answers generated using Cohere LLM
- Uses LangChain, FAISS, and Streamlit
- Metadata-aware responses
- Fast retrieval with cached vector index

## 🛠️ Built With

- 🧠 [LangChain](https://www.langchain.com/)
- 💬 [Cohere LLM](https://cohere.com/)
- ⚡ [FAISS](https://github.com/facebookresearch/faiss)
- 🖼️ [Streamlit](https://streamlit.io/)
- 📄 [PyPDFLoader](https://docs.langchain.com/docs/modules/data_connection/document_loaders/pdf)

## 🎥 Demo Video

[▶️ Watch the 1-minute demo](https://www.loom.com/share/5a2b36f808d94554b3478ca622de7832?sid=66bea12f-cdc4-4864-be6d-e9b2952a5c90) 


## 📂 Project Structure
chatbot/
├── app.py
├── ui.py
├── embedded.py
├── pdf_to_text.py
├── custom_prompt.py
├── data/
└── .env


## ✅ How to Run

1. Clone the repo
2. Add your Cohere API key to `.env`
3. Install requirements
4. Run Streamlit UI

```bash
streamlit run ui.py


