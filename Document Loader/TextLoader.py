from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser 



load_dotenv()   


model = ChatGroq(model_name="llama-3.1-8b-instant")
output_parser = StrOutputParser()
prompt = PromptTemplate(
    template="Give me a summary of this document: {doc}",
    input_variables=["doc"]
)


# loader = TextLoader("FIFA.txt", encoding="utf-8")
loader = TextLoader("Hugging.txt", encoding="utf-8") 
doc = loader.load() 
# path of the file must be given 
print(doc)
print(len(doc))

chain = prompt | model | output_parser 
result = chain.invoke({"doc": doc[0].page_content})

print(result)
