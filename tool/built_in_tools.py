from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

search_tool = DuckDuckGoSearchRun()


result = search_tool.invoke("What is the capital of France?")
print(result)

shell_tool = ShellTool()
result2 = shell_tool.invoke("pwd")
print(result2)

print(search_tool.args)