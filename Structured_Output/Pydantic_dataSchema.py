from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from typing import List,Optional
from dotenv import load_dotenv
from langchain_groq import ChatGroq
   
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

model_groq = ChatGroq(model_name="llama-3.1-8b-instant")


class Review(BaseModel):
    summary : str = Field(description="Create a summary for the given data.")
    sentiment : str = Field("either positive or negative for positive return pos and for negative return neg")
    author: Optional[str] = None
    reviewScore : float = Field(gt=0,lt=10, description="How helpful is this review based on the data provided inside it.")
    pros : list[str] = Field(description="List some pros from the product.")
    cons : list[str] = Field(description="List some cons from the product.")

structure = model_groq.with_structured_output(Review)

UserReview = """
It's crazy seeing how much praise and hype the S24 and S24+ are getting here. I'm guessing not many use the cameras (which is fine if it's not a need or priority) or have ever used another manufacturer with better camera hardware/processing.

Using a Pixel vs base model S22-24 series devices is extremely jarring, and a lot of techtuber reviewers that I've seen don't put these base models into scenarios where I feel like these cameras systems are challenged. And don't get me started on how awful the S22-S24 10MP 3x telephoto lens is.

If the S24+ has an MSRP of $999 (ignoring trade-ins, that is market dependent), it's priced above the cheapest P8P and OP12. I expect a ton more than finally getting a 1440p screen and 12GB RAM that should have been there in the S21+ to now. Samsung has their consumer base in a bit of a trap. Everytime you go to try something else, they offer insane pre-order deals and trade-ins with tons of carrier support. 

I expect more out of this community than benchmark score hype. That's what it's devolved to.
"""

result = structure.invoke(UserReview)

print(result)
   