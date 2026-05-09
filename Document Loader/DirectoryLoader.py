from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
load_dotenv()

loader = DirectoryLoader(path="Books" , 
                        glob="*.pdf",
                        loader_cls=PyPDFLoader)
docs = loader.load()

print(len(docs))
print(docs[167].page_content)
print(docs[167].metadata)