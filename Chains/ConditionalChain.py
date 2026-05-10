# from langchain_groq import ChatGroq
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnableBranch
# from langchain_core.output_parsers import StrOutputParser
# from langchain_nvidia_ai_endpoints import ChatNVIDIA
# from langchain_openai import ChatOpenAI
# import os




# load_dotenv()

# # model = ChatGroq(model_name = "llama-3.1-8b-instant") 

# # base_url="https://api.minimaxi.chat/v1"
# model2 = ChatOpenAI(
#     model="MiniMax-M2.7",
#     base_url="https://api.minimaxi.chat/v1",
#     api_key=os.getenv("MINIMAX_API_KEY")
# )
# parser = StrOutputParser()

# math_prompt = PromptTemplate(
#     input_variables = ["expression"],
#     template = "You are a math expert from MIT solve this {expression}"
# )

# math_chain = math_prompt | model2 | parser

# coding_prompt = PromptTemplate(
#     input_variables = ["code"],
#     template = "You are an expert python developer . Write a code to check if the {code} works or not."
# )

# coding_chain = coding_prompt | model2 | parser

# general_prompt = PromptTemplate(
#     template="""
# Answer this general question:
# {question}
# """,
#     input_variables=["question"]
# )

# general_chain = general_prompt | model2 | parser



# branch = RunnableBranch(
#     (lambda x:any(word in x["question"].lower()
#         for word in ["solve", "math", "+", "-", "*", "/"]),
#         math_chain),

#     (lambda x:any(word in x["question"].lower()
#         for word in ["python","java"]),
#         coding_chain),

#     general_chain

# )


# result = branch.invoke({"question":"write the code to calculate area of a triangle."})

# print(result)


from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os
load_dotenv()

client = ChatNVIDIA(
  model="minimaxai/minimax-m2.7",
  api_key= os.getenv("MINIMAX_API_KEY")
)


messages=[
  {
    "role": "user",
    "content": "Hello, how are you?"
  }
]

for chunk in client.stream(messages):
  print(chunk.content, end="")

