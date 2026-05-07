from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated


load_dotenv()

class Review(TypedDict):
   key_points : Annotated[list[str],"Here extract some of the key points mentioned in the message."]
   product_category : Annotated[str,"category of the product"]  
   pros : Annotated[str,"List some pros from the product."]
   cons : Annotated[str,"List some cons from the product."]
   author_name: Annotated[
    str,
    "Extract the author's name from the review."
    "If no author name is mentioned, return exactly 'Not Available'."
    ]

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
review_template = model.with_structured_output(Review)


prompt = """
Battery life is another major highlight. The 5000mAh battery easily lasts an entire day even with heavy usage including gaming, camera usage, social media, YouTube, and navigation. On moderate usage, I was even able to stretch it close to two days. Samsung finally nailed battery optimization here, and the Snapdragon chip plays a huge role in that. The standby battery drain is also very low compared to previous Galaxy devices.

The display is simply outstanding. The 6.8-inch Dynamic AMOLED 2X panel with 120Hz refresh rate looks gorgeous. Colors are vibrant, blacks are deep, and brightness outdoors is excellent. Watching Netflix, scrolling Instagram, or playing games feels incredibly immersive. Once you get used to this display quality, most other phones start looking average.

Now coming to the cameras — this is where the S23 Ultra really shines. The 200MP primary sensor captures an insane amount of detail, especially in daylight. Low-light photography is also excellent, and Samsung improved night mode a lot. The zoom capabilities are honestly crazy. The 3x and 10x optical zoom lenses are genuinely useful and not just marketing gimmicks. You can click clear moon shots, distant buildings, concerts, or portraits without losing too much quality. Video recording is also flagship level with excellent stabilization and sharpness

review by Priyanshu Paul
"""

result = review_template.invoke(prompt)
print(result)
