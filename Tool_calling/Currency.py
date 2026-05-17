from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.tools import tool
import requests
from langchain_core.messages import HumanMessage

load_dotenv() 

model = ChatGroq(model_name="llama-3.3-70b-versatile")

def get_exchange_rate(currency:str):
    """
    This function gets the exchange rate for a given currency.
    """
    
    url = f"https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data['rates'][currency]


from pydantic import BaseModel, Field

class CurrencyConverterInput(BaseModel):
    amount: float = Field(description="The amount of currency to convert")
    currency1: str = Field(description="The source currency code (e.g., USD)")
    currency2: str = Field(description="The target currency code (e.g., INR)")

@tool(args_schema=CurrencyConverterInput)
def calculate(amount: float, currency1: str, currency2: str) -> float:
    """
    This function calculates the exchange rate for a given currency. Here we convert amount from currency1 to currency2.
    """
    rate1 = get_exchange_rate(currency1)
    rate2 = get_exchange_rate(currency2)
    return amount * rate2 / rate1


exchange_model = model.bind_tools([calculate])


result = exchange_model.invoke("What is the exchange rate of 100 USD to INR?")
print("Content:", result.content)
print("Tool Calls:", result.tool_calls)   