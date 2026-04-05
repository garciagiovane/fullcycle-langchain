from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

model = init_chat_model(model_provider="openrouter", model="gemini-2.5-flash", temperature=0.5, name="Curso LangChain", max_tokens=15916)
message = model.invoke("Hello World")

print(message.content)