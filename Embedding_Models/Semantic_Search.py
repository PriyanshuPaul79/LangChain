from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

load_dotenv()

documents = [
    "the cat is sitting",
    "the dog is barking",
    "the kids are playing",
    "the stock market is booming"
]

prompt = input("Enter your prompt: ")

embeddings = HuggingFaceEndpointEmbeddings(
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model="sentence-transformers/all-MiniLM-L6-v2"
)

doc_vectors = embeddings.embed_documents(documents)
query_vector = embeddings.embed_query(prompt)

# similarities = cosine_similarity([query_vector], doc_vectors)[0]
# best_idx = np.argmax(similarities)

# print("Most similar:", documents[best_idx])

# print("here is the document vector:",doc_vectors)
# print("here is the query vector:",query_vector)

score = cosine_similarity([query_vector],doc_vectors)[0]
#[[ 0.55077514  0.45179759 -0.08312898  0.03239488]]

index,score = sorted(list(enumerate(score)), key=lambda x: x[1])[-1]

print(documents[index])
print(score)
#enumerate function returns the index and the value 
# then we sort the list usingg a lambda function which sort accordign to the value 

# this is the basic semantic search used in RAG in rag we will store the embeddings onces and then we use it but here every time we run our code embeddings are gettign generated every time.