from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure OpenAI service client 
client = OpenAI()

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment="gpt-3.5-turbo"

# add your completion code
prompt = "Şunu tamamlar mısın? Bir zamanlar çok güzel ve neşeli bir kız varmış. Bu kzın adı Zeynep Didarmış"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=1024, temperature=0.5)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
