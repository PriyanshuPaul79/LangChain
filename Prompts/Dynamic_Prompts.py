from  langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.7)
st.header("Hello")
# topic = st.text_input("Enter your topic")
# length = st.text_input("How long do you want")
# audience = st.text_input("Answer to whom ? ")

topic = st.selectbox("Select the topic", ["Dynamic programming","Greedy","Djikstra Shortest path","Floydd Warshell"])

style = st.selectbox("Select Explanantion type",["Beginner Friendly","Technical","Code oriented","Comedic"])

length = st.selectbox("Select the length of the result",["20-30 words","50-80 words","100-130 words"])

prompt = f"Write a summary about {topic} in {length} explain it in {style} manner."

#templete
# template = PromptTemplate(
#     template = """ our prompt along with the variables like this  {} """,
#     input_Variables = [our variables that we are using in this prompt like "Our input" and "Our length"],
# validate_template = True 
# this will validate the inputs in the prompt 

# ) 

# prompt = template.invoke({
#     map our variables with the input user is giving like 
#     "Our input":user_input,
#     "Our length" : user length
# })
 


if st.button('Summarize'):
    result = model.invoke(prompt)
    # later pass the prompt here
    st.write(result.content)