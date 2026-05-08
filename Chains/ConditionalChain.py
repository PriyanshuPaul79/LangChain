from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGroq(model_name = "llama-3.1-8b-instant")   
