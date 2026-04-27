from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.7)
# tempature tells us about the creativity of the model vary from 0 to 2 near 2 is more creative and near 0 is less creative

# max_completion_tokens tells us about the no. of tokens in output in pricy apis it limit the output so that we dont have to pay more to the api

result = llm.invoke("Hello list me 5 sports")
print(result.content)
