from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Annotated, Literal, Optional
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=1.2
)

class Review(BaseModel):
    key_things: list[str] = Field(description= 'write down all the key themes discussed in the review in a list')
    summary: str = Field(description= "A brief summary of the review")
    sentiment: Literal['pos', 'neg']
    pros: Optional[list[str]] = None
    cons: Optional[list[str]] = None
    name: Optional[str]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""
# iPhone Duo — Customer Review

**Reviewer Name:** Arjun Mehta

**Review Title:** An Impressive Device That Somehow Leaves Me Wanting More

**Rating:** 3.5/5

**Review:**

I've been using the iPhone Duo for nearly four months, and describing my experience as either good or bad would be an oversimplification. There are days when I genuinely appreciate how thoughtfully designed this device is, and others when I wonder whether I've simply become too comfortable accepting inconveniences from a product that costs considerably more than its competitors.

The first thing that impressed me was the overall design. The phone feels exceptionally premium, with a beautiful display, excellent build quality, and a comfortable grip. The interface is smooth, applications launch quickly, and multitasking rarely causes noticeable performance issues. However, I occasionally experience unexpected heating during video calls and gaming sessions. While this hasn't significantly affected my daily usage, it's difficult to ignore considering the price.

The camera is perhaps the most confusing aspect of the device. Daylight photography is outstanding, producing sharp images with excellent dynamic range and appealing colours. Portrait shots look particularly impressive. Yet nighttime photography sometimes feels overly processed, and certain images appear less natural than I would prefer. Interestingly, some of my friends consider these same photographs excellent, which makes me wonder whether the problem lies with the camera or simply my expectations.

Battery performance has been similarly inconsistent. On lighter days, I can comfortably get through an entire day without worrying about charging. However, when using navigation, recording videos, or switching frequently between applications, the battery drains noticeably faster. Charging isn't painfully slow, but it certainly doesn't feel revolutionary either. I suppose it's acceptable, although acceptable isn't exactly the word I expected to associate with a premium smartphone.

One thing Apple continues to do exceptionally well is software integration. Moving between compatible devices feels effortless, and the overall ecosystem creates a level of convenience that is genuinely difficult to abandon. At the same time, certain customization restrictions seem unnecessarily limiting. It's almost amusing how a device capable of handling demanding applications can occasionally make simple personal preferences feel complicated.

Despite these frustrations, I still enjoy using the iPhone Duo. It performs reliably for most everyday activities, feels polished, and delivers a consistently pleasant experience when everything works as intended. The difficulty is that its strengths are immediately noticeable, while its weaknesses reveal themselves gradually. None of those weaknesses are serious enough to make me dislike the phone, but together they make it harder to recommend without reservations.

Would I purchase it again? Probably, although that answer says as much about my familiarity with Apple's ecosystem as it does about the device itself. Would I recommend it to someone looking for the best value for money? That would require a much longer conversation.

Ultimately, the iPhone Duo feels like a product that delivers almost everything I expected while somehow leaving me questioning whether my expectations were high enough in the first place. I don't regret buying it, but I'm not entirely convinced that avoiding regret is the same thing as being satisfied.

## Pros

- Premium design with excellent build quality and comfortable handling.
- Smooth everyday performance and responsive multitasking.
- Impressive daylight photography and portrait shots.
- Beautiful display with sharp visuals and accurate colours.
- Seamless integration with other Apple devices.
- Reliable software experience for most everyday activities.
- Battery life is satisfactory under moderate usage.
- Consistently polished user interface.

## Cons

- Occasional heating during gaming and extended video calls.
- Nighttime photographs sometimes appear excessively processed.
- Battery drain becomes noticeable during demanding activities.
- Charging speeds feel underwhelming for the price.
- Limited customization compared with competing smartphones.
- Premium pricing makes minor inconveniences harder to overlook.
- Some ecosystem conveniences depend on owning additional Apple devices.
- Overall improvements don't always feel substantial enough to justify the expense.

""")

print(result)