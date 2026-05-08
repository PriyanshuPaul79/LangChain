from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field

load_dotenv()

# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
model2 = ChatGroq(model_name="llama-3.1-8b-instant")

class DiseaseSymptoms(BaseModel):
    name : str = Field(description="Name of the disease")
    days_to_heal : int = Field(description="How many days does this disease take to recover from.")
    cause : str = Field(description="what caused this disease.")
    


parser = JsonOutputParser(
    pydantic_object=DiseaseSymptoms
)

parser2 = PydanticOutputParser(
    pydantic_object=DiseaseSymptoms
)




prompt = PromptTemplate(
    template = "Your are a doctor give me info about  {disease} {format_instruction}",
    input_variables= ['disease'],
    partial_variables={"format_instruction": parser.get_format_instructions()
    }
)


prompt2 = PromptTemplate(
    template = "Your are a doctor give me info about  {disease} {format_instruction}",
    input_variables= ['disease'],
    partial_variables={"format_instruction": parser2.get_format_instructions()
    }
)

chain2 = prompt2 | model2 | parser2
result2 = chain2.invoke({"disease": "Diptheria"})
print(result2)
print(type(result2))


# chain = prompt | model2 | parser
# result = chain.invoke({"disease": "Diptheria"})
# print(type(result))



# steps are clear for using the parsers :-
# 1. create a parsers using JsonOutputParser or PydanticOutputParser 
# 2. create the promopt using the PromptTemplate 
# 3. inside that we have to format the output according to our parsers
# 4. in the prompt we need the dynamic input also include the {format_instructions} which tells the llm expected structure
# JSON format
# field names
# data types

# 5. create a chain 
# 6. invoke that chain 