from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda

load_dotenv()

model1 = ChatGoogleGenerativeAI(model= "gemini-3.6-flash")

model2 = ChatGoogleGenerativeAI(model= "gemini-3.7-flash")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template= 'Classify the sentiment of the following feedback into positive or negative\n{feedback}',
    input_variables= ['feedback']
)

prompt2 = PromptTemplate(
    template= 'Write appropriate response to this positive feedback\n{feedback}',
    input_variables= ['feedback']
)

prompt3 = PromptTemplate(
    template= 'Write appropriate response to this negative feedback\n{feedback}',
    input_variables= ['feedback']
)

classifier_chain = prompt1 | model2 |parser

branch_chain = RunnableBranch(
    (lambda x : x == 'Positive', prompt2 | model2 | parser),
    (lambda x : x == 'Negative', prompt3 | model2 | parser),
    RunnableLambda(lambda x : "Could not find the sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': "this is a good phone"})

print(result)

chain.get_graph().print_ascii()