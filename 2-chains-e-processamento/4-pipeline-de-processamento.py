from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template = PromptTemplate(
    input_variables=["initial_text"],
    template="Translate the following text to English:\n ```{initial_text}```"
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words:\n ```{text}```"
)

model = ChatOpenRouter(
    model="openai/gpt-5-mini", 
    temperature=0, 
    name="Curso LangChain",
    max_tokens=19237
)

translation = template | model | StrOutputParser()
pipeline = {"text": translation } | template_summary | model | StrOutputParser()
result = pipeline.invoke({"initial_text": "Langchain é um framework para desenvolvimento de aplicações de IA."})
print(result)


