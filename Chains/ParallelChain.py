from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGroq(model_name = "llama-3.1-8b-instant")   
model2  = ChatGroq(model_name = "openai/gpt-oss-120b")

class Market(BaseModel):
    sentiment: str = Field(description="either bullish or bearish")
    reason : str = Field(description = "reason for the sentiment")
    score : int = Field(description = "score out of 10")

structured_model = model.with_structured_output(Market)
structured_model2 = model2.with_structured_output(Market)

prompt = PromptTemplate(
    template = """
    You are a market analyst. Analyse the market sentiment for the given stock.
    
    Stock : {stock}
    """,
    input_variables = ["stock"]
) 

prompt2 = PromptTemplate(
    template = """
    You are a seasoned Wall Street trader with 20 years of experience navigating market crises.
    
    BREAKING NEWS: The CEO of {stock} has just been arrested on charges of financial fraud.
    Markets open in 10 minutes. Your fund has a significant position in {stock}.
    
    You have one shot to make the right call. Based on this news, analyze the situation:
    - What is your gut sentiment on the stock right now?
    - What is your immediate trading strategy and why?
    - Rate the urgency and severity of this event out of 10.
    
    Think fast. The clock is ticking.
    """,
    input_variables = ["stock"]
)

chain1 = prompt | structured_model
chain2 = prompt2 | structured_model2

chain3 = RunnableParallel(
    market_analyst = chain1,
    trader = chain2
)

result = chain3.invoke({"stock": "tesla"})
print(result)