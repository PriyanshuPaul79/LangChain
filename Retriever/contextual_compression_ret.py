import os
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_chroma import Chroma  # Updated to the dedicated package
from langchain_huggingface import HuggingFaceEndpointEmbeddings

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

from langchain_groq import ChatGroq

# 1. Load environment variables (Make sure GROQ_API_KEY and HUGGINGFACEHUB_API_TOKEN are set)
load_dotenv()

# 2. Initialize LLM (Groq is great for this as it's fast)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# 3. Compressor: Extracts only the relevant parts of documents
compressor = LLMChainExtractor.from_llm(llm)

# 4. Sample Documents
docs = [
    Document(page_content="Artificial intelligence is transforming healthcare through predictive diagnostics and automated medical imaging analysis."),
    Document(page_content="Contextual compression retrievers optimize retrieval systems by filtering irrelevant information."),
    Document(page_content="Cloud computing enables scalable infrastructure for modern software applications."),
    Document(page_content="Machine learning algorithms learn patterns from data to make predictions."),
    Document(page_content="Cybersecurity practices protect systems and sensitive information from digital attacks.")
]

# 5. Fixed Embeddings: Added the 'task' parameter which is often required by the Endpoint API
embedding_model = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
    task="feature-extraction", 
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

# 6. Vector Store: Using langchain_chroma for better stability
# Added a collection_name and used a temporary in-memory setup
vector_store = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    collection_name="security_docs"
)

# 7. Base Retriever
similarity_retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# 8. Compression Retriever
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=similarity_retriever
)

# 9. Execution
query = "How can AI help with medical safety and diagnostics?"

print(f"\nQuery: {query}\n")

# Compressed Retrieval
results = compression_retriever.invoke(query)

print("===== COMPRESSED RESULTS =====")
if not results:
    print("No relevant snippets found after compression.")
for doc in results:
    print(f"- {doc.page_content}")

# Normal Retrieval
similarity_results = similarity_retriever.invoke(query)

print("\n===== NORMAL (RAW) RESULTS =====")
for doc in similarity_results:
    print(f"- {doc.page_content}")