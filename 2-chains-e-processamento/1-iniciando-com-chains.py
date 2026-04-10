from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

template = PromptTemplate(
    input_variables=["name"],
    template="Hi, i'm {name}! Tell me a joke with my name"
)

model = ChatOpenRouter(model="openai/gpt-5-nano", temperature=0.5, name="Curso LangChain")

chain = template | model

result = chain.invoke({"name": "Giovane"})
print(result.content)
