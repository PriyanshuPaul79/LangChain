from langchain_huggingface import HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated

load_dotenv()

# model = HuggingFaceEndpoint(
#     repo_id="Qwen/Qwen2.5-7B-Instruct",
#     task="conversational",
#     max_new_tokens=400,
#     temperature=0.7,
# ) 
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

# some hugging face models dont support with_structured_output function but the openai and the google ai support that 

class Review(TypedDict):
    summary : Annotated[str,"A breif summary of the review"]
    # annotated will guide the model what to do or what value of place in that key 
    sentiment : Annotated[int,"what is the sentiment of this review "]

structure = model.with_structured_output(Review)

# model  ─────▶ normal text output
# structure ─────▶ model + schema enforcement
# structure.invoke(input)

result = structure.invoke("""The design of this phone is sleek and premium-looking—I get compliments on it all the time. Performance is fast for daily tasks, and multitasking is smooth. That said, the battery drains faster than expected, especially with heavy use. Also, the software has a few annoying pre-installed apps you can’t remove.""")

print(result)