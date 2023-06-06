
from dotenv import load_dotenv
load_dotenv()
import os
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain


openai_api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=['something'],
    template='{something} に必要なスキルは何?'
)

chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run(something="AGI開発"))