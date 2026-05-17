from langchain_text_splitters import RecursiveCharacterTextSplitter,Language
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import os

load_dotenv()

# loader = PyPDFLoader("../Document Loader/Books/Designing Machine Learning Systems.pdf")
# docs = loader.load()


text = """
My name is Priyanshu
I am 22 years old

I live in Kolkata

My favorite color is blue
I am a student
I am a developer
"""
# text_splitter = RecursiveCharacterTextSplitter(
#     separators = ["\n\n", "\n", " "],
#     chunk_size = 1000,
#     chunk_overlap = 200
# )


code = """
import java.util.*;
public void hello(){
system.out.println("Hello");
}
public class Main{
    public static void main(String[] args){
        hello();
    }
}
"""

text_splitter3 = RecursiveCharacterTextSplitter.from_language(
    language= Language.JAVA,
    chunk_size= 100,
    chunk_overlap = 0
)

result3 = text_splitter3.split_text(code)
print(result3)


# text_splitter2 = RecursiveCharacterTextSplitter(
#     separators=["\n\n", "\n", "."],
#     chunk_size=40,
#     chunk_overlap=5
# )

# result2 = text_splitter2.split_text(text)
# print(result2)


# result = text_splitter.split_documents(docs)

# print(len(result))
# print(result[198])