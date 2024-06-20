from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure Azure OpenAI service client 
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']
  )

#deployment=os.environ['OPENAI_DEPLOYMENT']
deployment="gpt-3.5-turbo"

# add your completion code
question = input("Bankacılık konusunda öğrenmek istediklerini bana sorabilirsin: ")
prompt = f"""
Bankacılık konusunda 30 yıllık tecrübe ile bana yardımcı olabilir misin?

Sana sorulan sorulara cevap verirken aşağıdaki formatta cevaplayabilir misin?:

- Konseptin tanımı
- Örnekler ile konseptin nasıl yapıldığının açıklaması kullanıcı tarafından daha iyi anlaması için.
- Konsepte yakın 2-3 adet benzer başlıkların listelenmesi

Şu soru için cevap verebilir misin?: {question}
"""
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)
