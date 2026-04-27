from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# We use Qwen-Chat which is EXTREMELY reliable on the Hugging Face Chat API
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    max_new_tokens=400,
    temperature=0.7,
)

# Qwen is a dedicated Chat model so ChatHuggingFace will work perfectly
model = ChatHuggingFace(llm = llm)

print("Querying Qwen-7B-Instruct...")
result = model.invoke(input("Enter your query: "))

print("\nResult:")
print(result.content)