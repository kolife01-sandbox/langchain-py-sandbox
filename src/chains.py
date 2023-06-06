
from dotenv import load_dotenv
load_dotenv()
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain


openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=['product'],
    template='What would be a good company name for a company that makes {product}?'
)

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run(product="colorful socks"))