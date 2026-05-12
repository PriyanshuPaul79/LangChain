from langchain_nvidia_ai_endpoints import ChatNVIDIA
import os
from dotenv import load_dotenv

load_dotenv()
model = ChatNVIDIA(
    model="minimaxai/minimax-m2.7",
    api_key=os.getenv("NVIDIA_NIM")
)

try:
    print(model.invoke("hello").content)
except Exception as e:
    print(f"Error: {e}")
