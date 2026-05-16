from langchain_core.tools import tool
@tool
def add(a:int,b:int)->int:
    """
    This function adds two numbers.
    """
    return a+b

@tool
def sub(a:int,b:int)->int:
    """
    This function subtracts two numbers.
    """
    return a-b

@tool
def mul(a:int,b:int)->int:
    """
    This function multiplies two numbers.
    """
    return a*b

@tool
def div(a:int,b:int)->int:
    """
    This function divides two numbers.
    """
    return a/b



class MathToolKit:
    # def add(self,a:int,b:int)->int:
    #     """
    #     This function adds two numbers.
    #     """
    #     return a+b
    
    # def sub(self,a:int,b:int)->int:
    #     """
    #     This function subtracts two numbers.
    #     """
    #     return a-b
    
    # def mul(self,a:int,b:int)->int:
    #     """
    #     This function multiplies two numbers.
    #     """
    #     return a*b
    
    # def div(self,a:int,b:int)->int:
    #     """
    #     This function divides two numbers.
    #     """
    #     return a/b


    def getTools(self):
        return [add,sub]




tools_needed = MathToolKit().getTools()
# print(tools_needed)

ans = tools_needed[0].invoke({"a":10,"b":20})
print(ans)