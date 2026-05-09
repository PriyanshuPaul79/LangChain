from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

loader = PyPDFLoader("ovw-short.pdf")
docs = loader.load()
print(docs[7].page_content)
print(docs[7].metadata)
print(len(docs))


# PypdfLoader is good for textual pdf 
# not good for scanned pdf 

# for pdf with tables and columns PDFPlumberLoader
# for scanned images pdf UnstructuredPDFloader or AmazonTextractPDFLoader 