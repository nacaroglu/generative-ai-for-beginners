from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure Azure OpenAI service client 
client = OpenAI()

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment="gpt-3.5-turbo"

no_questions = input("Soru sayısını giriniz:(örneğin, 5): ")
course = input("Ders: giriniz: (örneğin, matematik, coğrafya): ")
topic = input("Konu: giriniz: (örneğin, doğal sayılar, Türkiye'nin illeri): ")
grade = input("Sınıf: giriniz: (örneğin, 5, 6, 7): ")

# interpolate the number of recipes into the prompt an ingredients
prompt = f"Benim için {course} dersinden {topic} konuları kapsayan, {no_questions} adet {grade} sınıf için soru hazırlar mısın?: "
messages = [{"role": "user", "content": prompt}]

completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=2048, temperature = 0.5)

questions = completion.choices[0].message.content

# print response
print("Sorular:")
print(questions)


new_prompt = f"Rica etsem şu soruların cevaplarını detaylı biçimde açıklar mısın? {questions}"
messages = [{"role": "user", "content": new_prompt}]
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=4096, temperature=0)

# print response
print("\n=====Cevaplar ======= \n")
print(completion.choices[0].message.content)





