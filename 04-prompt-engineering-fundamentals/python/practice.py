# The OpenAI SDK was updated on Nov 8, 2023 with new guidance for migration
# See: https://github.com/openai/openai-python/discussions/742

## Updated
import os
from openai import OpenAI
import tiktoken


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-3.5-turbo"
#model = "gpt-4-turbo"

## Updated
def get_completion(prompt):
    messages=[{"role": "user", "content": prompt}]       
    response=client.chat.completions.create(   
        model=model,                                     
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
        max_tokens=1024
    )
    return response.choices[0].message.content

def practice_1():
    # Define the prompt you want tokenized
    text = f"""
    Jupiter is the fifth planet from the Sun and the \
    largest in the Solar System. It is a gas giant with \
    a mass one-thousandth that of the Sun, but two-and-a-half \
    times that of all the other planets in the Solar System combined. \
    Jupiter is one of the brightest objects visible to the naked eye \
    in the night sky, and has been known to ancient civilizations since \
    before recorded history. It is named after the Roman god Jupiter.[19] \
    When viewed from Earth, Jupiter can be bright enough for its reflected \
    light to cast visible shadows,[20] and is on average the third-brightest \
    natural object in the night sky after the Moon and Venus.
    """

    # Set the model you want encoding for
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    # Encode the text - gives you the tokens in integer form
    tokens = encoding.encode(text)
    print(tokens);

    # Decode the integers to see what the text versions look like
    [encoding.decode_single_token_bytes(token) for token in tokens]

def practice_2():
    ### 1. Set primary content or prompt text
    text = f"""
    İşta bak sana dememişmiydim, Maraş'ın çok tehlikeli deprem bölgesi olduğunu.
    """

    ### 2. Use that in the prompt template below
    prompt = f"""
    ```{text}```
    """

    ## 3. Run the prompt
    response = get_completion(prompt)
    print(response)

def practice_3():
    ## Set the text for simple prompt or primary content
    ## Prompt shows a template format with text in it - add cues, commands etc if needed
    ## Run the completion 
    text = f"""
    generate a lesson plan on the Martian War of 2076.
    """

    prompt = f"""
    ```{text}```
    """

    response = get_completion(prompt)
    print(response)

def practice_4():
    # Test Example
    # https://platform.openai.com/playground/p/default-summarize

    ## Example text
    text = f"""
    Ben edebiyatı kendime dert edinmiş bir adamım.\
    Gece gündüz edebiyat düşünürüm. Sevdiğim bir şiiri tanıdıklarıma okumadığım veya edebiyat sorunu üzerine \
    tartışmaya girmediğim, yazmadığım günler yaşadım \
    saymam kendimi. “Bugün Türkiye’de en tam edebiyat \
    adamı kimdir?” diye sorarlarsa beni gösterebilirsiniz. \
    Övünmek için söylemiyorum bunu, yazdıklarım iyidir, \
    kötüdür o başka, iyiyse de kötüyse de inanarak yazarım, 
    övmem de yermem de bir çıkar kaygısıyla, dostluk, arkadaşlık düşüncesiyle değildir 
    """

    ## Set the prompt
    prompt = f"""
    Böyle konuşan bir kişi aşağıdakilerden hangisiyle nitelendirilemez?  
    A) Bencil B) Özgüvenli C) Çalışkan D) Üretken  E) Sorgulayıcı
        ```{text}```
    """

    ## Run the prompt
    response = get_completion(prompt)
    print(response)    

#practice_1()
#practice_2()
#practice_3()
#practice_4()

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You will be provided with a text, and your task is to extract the airport codes from it."},
        {"role": "user", "content": "Turkish: SAbiha GökŞEN to Kahramanmaraş'a"},        
        
    ]
)
print(response.choices[0].message.content)




