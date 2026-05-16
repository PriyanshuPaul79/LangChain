# 1 using @tool decorator

# from langchain_core.tools import tool


# @tool
# def add(a:int,b:int)->int:
#     """
#     This function adds two numbers.
#     """
#     return a+b


# @tool
# def subtract(a:int,b:int)->int:
#     """
#     This function subtracts two numbers.
#     """
#     return a-b

# @tool
# def multiply(a:int,b:int)->int:
#     """
#     This function multiplies two numbers.
#     """
#     return a*b


# @tool
# def divide(a:int,b:int)->int:
#     """
#     This function divides two numbers.
#     """
#     return a/b


# result = add.invoke({"a":45,"b":49})
# print(result)
# print(divide.args)


# 2. creating tools using pydantic structured tool
# from langchain_core.tools import StructuredTool
# from pydantic import BaseModel,Field

# class Calculator(BaseModel):
#     a:int = Field(description="The first number")
#     b:int = Field(description="The second number")
    
# def divide(a,b):
#     return a/b

# div_tool = StructuredTool.from_function(
#     func=divide,
#     name="divide",
#     description="This function divides two numbers.",
#     args_schema=Calculator
# )

# result2 = div_tool.invoke({"a":40.29,"b":2})
# print(result2)
    
