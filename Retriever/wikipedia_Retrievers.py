from langchain_community.retrievers import WikipediaRetriever
import wikipedia # Import the wikipedia library

wikipedia.set_user_agent("my-langchain-app/1.0 (https://example.com)") # Set a user agent
ret1 = WikipediaRetriever(top_k_results = 2,lang="en")

query = "Shree Ram"
answer = ret1.invoke(query) 
print(answer)
# we can use inovke function as it elong to runnable class.
for i,doc in enumerate(answer):
    print(f"\n  Result {i+1} .....")
    print(f" Content {doc.page_content}")
