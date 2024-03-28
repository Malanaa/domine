import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = input("Provide your Google API Key")

llm = ChatGoogleGenerativeAI(model="gemini-pro")

result = llm.invoke("Hello this is a test message.")
print(result.content)