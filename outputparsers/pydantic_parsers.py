from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import Field, BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

class Person(BaseModel):

    name: str = Field(description="Name of the person")
    age: int = Field(gt= 18, description="Age of the person")
    place: str = Field(description="Place of the person belongs to")

parser = PydanticOutputParser(pydantic_object= Person)

template = PromptTemplate(
    template= "Generate the name, age and place of a fictional character from {place}\n{format_instruction}",
    input_variables= ['place'],
    partial_variables = {'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'place': 'India'})

print(result)
chain.get_graph().print_ascii()