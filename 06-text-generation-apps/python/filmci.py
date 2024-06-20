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
deployment="gpt-4-turbo"

# add your completion code
print("İstersen birlikte izleyeceğin filmi seçebiliriz")
genre = input("Hangi tip filimlerden hoşlanırısın? (örn: aksiyon, komedi, romantik, bilim kurgu): ")
year_range = input("Hangi yıllar arasında çekilmiş filmleri izlemek istersin? (örn: 2000-2010): ");
country = input("Hangi ülkenin filmlerini izlemek istersin? (örn: Türkiye, ABD, Fransa): ");
director = input("Hangi yönetmenin filmlerini izlemek istersin? (örn: Steven Spielberg): ");

selection = f"Filmin türü: {genre}, yıl aralığı: {year_range}, ülke: {country}"
if director:
    selection += f", yönetmen: {director}"
    

prompt = f"""
  Film seçmek istiyorum ve senin zevkine güveniyorum?
  Kriterler: {selection} filimler arasından 5 tane en tercih ettiklerinin arasından seçmek istiyorum.
  Bana bunları siralar adi, yili, türü, ülkesi, yönetmeni ve başrol oyuncularını içerecek şekilde JSON formatında 
  sıralar mısın?
"""

messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
print(completion.choices[0].message.content)
