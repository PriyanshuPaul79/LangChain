from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os

load_dotenv()

model = ChatNVIDIA(
    model = "minimaxai/minimax-m2.7",
    api_key = os.getenv("NVIDIA_NIM")
)

# result = model.invoke("Hello")
# print(result)


model2 = ChatGroq(
    model = "llama-3.1-8b-instant",
    api_key = os.getenv("GROQ_API_KEY")
)

result2 = model2.invoke("Hello")
print(result2.content)

# prompt = PromptTemplate(
#     input_variables = ["document"],
#     template = """
#     Summarise the following document in 3 bullet points based on the context provided:
#     {document}
#     """
# )



# loader = PyPDFLoader("./Books/Designing Machine Learning Systems.pdf")
# docs = loader.load()

# chain = prompt | model | StrOutputParser()
# result = chain.invoke({"document":docs[0].page_content}) 

# print(result)


# print(docs[7].page_content)
# print(docs[7].metadata)
# print(len(docs))


# PypdfLoader is good for textual pdf 
# not good for scanned pdf 

# for pdf with tables and columns PDFPlumberLoader
# for scanned images pdf UnstructuredPDFloader or AmazonTextractPDFLoader 

