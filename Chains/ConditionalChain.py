from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model_name = "llama-3.1-8b-instant")   

parser = StrOutputParser()

math_prompt = PromptTemplate(
    input_variables = ["expression"],
    template = "You are a math expert from MIT solve this {expression}"
)

math_chain = math_prompt | model | parser

coding_prompt = PromptTemplate(
    input_variables = ["code"],
    template = "You are an expert python developer . Write a code to check if the {code} works or not."
)

coding_chain = coding_prompt | model | parser

general_prompt = PromptTemplate(
    template="""
Answer this general question:
{question}
""",
    input_variables=["question"]
)

general_chain = general_prompt | model | parser



branch = RunnableBranch(
    (lambda x:any(word in x["question"].lower()
        for word in ["solve", "math", "+", "-", "*", "/"]),
        math_chain),

    (lambda x:any(word in x["question"].lower()
        for word in ["python","java"]),
        coding_chain),

    general_chain

)


result = branch.invoke({"question":"write the code to calculate area of a triangle."})

print(result)