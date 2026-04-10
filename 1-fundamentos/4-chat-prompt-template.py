from langchain_core.prompts import ChatPromptTemplate
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
load_dotenv()

system = ("You are an assistant that answers questions in a {style} style.")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])
messages = chat_prompt.format_messages(style="funny", question="Who is Alan Turing?")

for message in messages:
    print(f"{message.type}: {message.content}")

model = ChatOpenRouter(model="openai/gpt-5-nano", temperature=0.5, name="Curso LangChain")
response = model.invoke(messages)
print(response.content)