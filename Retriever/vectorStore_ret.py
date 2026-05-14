from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from dotenv import load_dotenv

load_dotenv()

docs = [
    Document(page_content="Hello Homelander you can fly"),
    Document(page_content="Hello Deep you can swim"),
    Document(page_content="Hello Sage great memory"),
    Document(page_content="Hello Kimiko great regeneration")
]

embedding = HuggingFaceEndpointEmbeddings(
model="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    collection_name="my_collection"
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

result = retriever.invoke("who play with fishes?")

print(result[0].page_content)