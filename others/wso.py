from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=1.2
)

class Review(TypedDict):
    summary: Annotated[str, 'A brief summary of the review']
    sentiment: Annotated[Literal["positive", 'negative', 'neutral'], 'Return sentiment of the review either negative, positive or neutral']

structured_model = model.with_structured_output(Review, method=json)

result = structured_model.invoke("""
The hardware is great but the software feels bloated.
There are too many pre-installed apps that I can't remove.
Also the UI looks outdated compared to other brands.
Hoping for a software update to fix this.
""")

print(result)