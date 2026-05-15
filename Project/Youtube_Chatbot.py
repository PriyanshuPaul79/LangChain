from langchain_groq import ChatGroq 
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from youtube_transcript_api import YouTubeTranscriptApi
import os
import json



load_dotenv()

# models needed
model_groq = ChatGroq(model_name="llama-3.1-8b-instant")
embedding_model = HuggingFaceEndpointEmbeddings(
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model="sentence-transformers/all-MiniLM-L6-v2"
)

# step 1: load youtube transcript
video_id = str(input("Enter Youtube Video ID:"))
try:
    transcript = YouTubeTranscriptApi().fetch(video_id,languages=["en"])
    text = " ".join([segment.text for segment in transcript])

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

    docs = splitter.split_text(text)


    vector_store = FAISS.from_texts(
        texts=docs,
        embedding=embedding_model
    )



    retriever = vector_store.as_retriever(
        search_kwargs={"k":3},
        search_type="similarity"
    )

    query = input("Ask something: ")
    result = retriever.invoke(query)
    # print(result)

    prompt = PromptTemplate(
        template="""
        Your are a helpful assistent that answer questions based on the context provided. If the context is insufficient just directly say that the context is insufficient. Return nothing else.
        {context}
        Question: {question}
        """,
        input_variables=["context","question"]
    )

    question = input("Enter your question:")

    retrieved_docs = retriever.invoke(question)
    # print(retrieved_docs)

    context = " ".join([doc.page_content for doc in retrieved_docs])
    # print(context)

    final_prompt = prompt.invoke({"context":context,"question":question})
    # print(final_prompt.content)

    
    actual_answer = model_groq.invoke(final_prompt)
    print(actual_answer.content)

    # print(text)

    # transcript_json = [
    # {
    #     "text": segment.text,
    #     "start": segment.start,
    #     "duration": segment.duration
    # }
    # for segment in transcript
except Exception as e:
    print(e)


# print(json.dumps(transcript_json,indent=4))


# divide into chunks


# print(len(docs))
# print(docs[15])



# it give us the chunks along eith there ids and also tells us how the data is getting stored . 
# print(vector_store.index_to_docstore_id)

# print(f"here is the chunk we retrived:{vector_store.get_by_ids(['7681eb66-2ad2-4116-a3b8-dc1452277fcd'])}")

