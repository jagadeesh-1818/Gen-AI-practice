
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import (
    StructuredOutputParser,
    ResponseSchema
)

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

schema = [
    ResponseSchema(
        name="fact1",
        description="First fact about the topic"
    ),
    ResponseSchema(
        name="fact2",
        description="Second fact about the topic"
    ),
    ResponseSchema(
        name="fact3",
        description="Third fact about the topic"
    )
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 facts about {topic}\n{format_instruction}",
    input_variables=["topic"],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)

chain = template | model | parser

result = chain.invoke({"topic": "black holes"})

print(result)

chain.get_graph().print_ascii()