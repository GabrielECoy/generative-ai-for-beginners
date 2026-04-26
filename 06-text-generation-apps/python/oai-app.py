from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure OpenAI service client 
client = OpenAI()
deployment = "gpt-4o" #"gpt-3.5-turbo" - "gpt-5.5-pro" is not a chat model, so we can't use it for this example. You can use it for non-chat completions.

# add your completion code
# Roles
# system: Sets instructions, personality, and behavior for the (used by AI Developer)
# user: Questions or requests from the human (End user)
# assistant: Previous responses from the AI, for context in multi-turn conversations (System automatic)
prompt = "Complete the following: Once upon a time there was a"
messages = [{"role": "system", "content": "You are a person that writes short stories."}, {"role": "user", "content": prompt}, {"role": "assistant", "content": "I like stories that mix water and land"}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)


# print response
print(prompt,":",completion.choices[0].message.content)
from pprint import pprint
pprint(completion)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
