from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load env variables
load_dotenv()

app = FastAPI()

# Define request model
class PromptRequest(BaseModel):
    topic: str

# Output parser
output_parser = StrOutputParser()

# Essay chain using OpenAI
essay_prompt = ChatPromptTemplate.from_template("Write a 100-word essay about {topic}.")
essay_chain = essay_prompt | ChatOpenAI(model="gpt-4", temperature=0.7) | output_parser

# Poem chain using Anthropic
poem_prompt = ChatPromptTemplate.from_template("Write a 100-word poem about {topic}.")
poem_chain = poem_prompt | ChatAnthropic(model="claude-3-haiku-20240307", temperature=0.7) | output_parser

@app.post("/essay")
async def generate_essay(request: PromptRequest):
    result = await essay_chain.ainvoke({"topic": request.topic})
    return {"essay": result.strip()}

@app.post("/poem")
async def generate_poem(request: PromptRequest):
    result = await poem_chain.ainvoke({"topic": request.topic})
    return {"poem": result.strip()}

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)