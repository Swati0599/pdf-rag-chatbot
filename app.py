from langchain_community.llms import Cohere
from langchain.chains import RetrievalQA
from embedded import generate_retriver
from pdf_to_text import text_split
import os
from dotenv import load_dotenv
from custom_prompt import custom_prompt
load_dotenv()
import warnings
warnings.filterwarnings("ignore")

text_chunks = text_split()

llm = Cohere(
    cohere_api_key=os.getenv("COHERE_API_KEY"),
    temperature=0.1
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=generate_retriver(text_chunks),
    chain_type="stuff",
    chain_type_kwargs={"prompt": custom_prompt}
)

while True:
    question = input("Ask something (or type 'exit'): ")
    if question.lower() == "exit":
        break
    response = qa_chain.invoke({"query": question})
    print("\n🧠 Answer:\n", response["result"].strip(), "\n")
    

