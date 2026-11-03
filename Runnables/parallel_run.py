from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model= "gemini-3.8-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template= "Write a 200 words tweeter post about the {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Write a 200 words linkedin post about the {topic}",
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'tweet' : prompt1 | model1 | parser,
    'linkedin' : prompt2 | model1 | parser
})

print(parallel_chain.invoke({'topic': "AI"}))