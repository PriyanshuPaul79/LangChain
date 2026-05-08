from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGroq(model_name = "llama-3.1-8b-instant")   


class Fruit(BaseModel):
    name : str = Field(description="The name of the fruit")
    thing : str = Field(description="name a thing of that color.")

structured_model = model.with_structured_output(Fruit)

Prompt = PromptTemplate(
    template = """
    The user will give you a color. Return a fruit of that color and name a thing of that color.
    
    Color: {color}
    """,
    input_variables = ["color"]
)

# prompt2 = PromptTemplate(
#     template = """
    
#     """,
#     input_variable = ["fruit"],
#     partial_variables={
#         "format_instruciton": parser.get_format_instructions()
#     }
# )


chain = Prompt | structured_model
result = chain.invoke({'color':'Red'})
print(result)