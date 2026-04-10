from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import chain
from dotenv import load_dotenv
load_dotenv()

@chain
def square(x: dict) -> dict:
    value = x["x"]
    return {"square_result": value * value}

template2 = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me about the number {square_result}"
)

model = ChatOpenRouter(
    model="openai/gpt-5-nano", 
    temperature=0.5, 
    name="Curso LangChain"
)

chain2 = square | template2 | model

result = chain2.invoke({"x": 10})
print(result.content)