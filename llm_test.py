import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
HF_token=os.getenv("HF_TOKEN")

client=OpenAI(base_url="https://router.huggingface.co/v1",api_key=HF_token)
response=client.chat.completions.create(model="openai/gpt-oss-120b",
                               messages=[{
                                   "role":"user",
                                   "content":"What is good source of protein in Vegetarian.and prepare a meal plan for me."
                               }])

answer=(response.choices[0].message.content)
print(answer)