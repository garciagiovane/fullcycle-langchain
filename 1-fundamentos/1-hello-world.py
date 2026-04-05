from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
load_dotenv()

model = ChatOpenRouter(model="openai/gpt-5-nano", temperature=0.5, name="Curso LangChain")
message = model.invoke("Hello World")

print(message.content)