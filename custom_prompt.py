from langchain.prompts import PromptTemplate

custom_prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an intelligent assistant answering only based on the provided document context.

Instructions:
- Give clear, natural answers.
- Do not mention document filenames or sources in your response.
- If the answer is not found, respond with: "Not found in the document."

Context:
{context}

Question:
{question}

Answer:
"""
)
