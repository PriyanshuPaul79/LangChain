from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7 )

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational",
    max_new_tokens=400,
    temperature=0.7,
)
model = ChatHuggingFace(llm=llm)

while True:
    user_input = input("Priyanshu : ")
    if user_input == "End":
        break
    result = model.invoke(user_input)
    print("Friday: ",result.content)
