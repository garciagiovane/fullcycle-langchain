from langchain_core.runnables import RunnableLambda

def parseNumber(text: str) -> int:
    return int(text.strip())

parse_runnable = RunnableLambda(parseNumber)

number = parse_runnable.invoke(" 10 ")
print(number)