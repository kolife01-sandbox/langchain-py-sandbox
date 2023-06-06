from dotenv import load_dotenv
load_dotenv()
import os
from langchain.llms import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=openai_api_key, temperature=0.9)

text = "What would be a good company name for a company that makes colorful socks?"
print(llm(text))