import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY","")
assert API_KEY, "ERROR: OpenAI Key is missing"

client = OpenAI(api_key=API_KEY)

model = "gpt-4-turbo"

def first_promt():

    # Create your first prompt
    text_prompt = "Should oxford commas always be used?"

    response = client.chat.completions.create(
    model=model,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content":text_prompt},])

    result = response.choices[0].message.content
    print(result)

    response = client.chat.completions.create(
    model=model,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content":text_prompt},])

    result = response.choices[0].message.content
    print(result)

def process_text(prompt):

    response = client.chat.completions.create(
    model=model,
    messages = [{"role":"system", "content":"You are a helpful assistant."},
                {"role":"user","content":prompt},])

    print(response.choices[0].message.content)


#prompt = "Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something that current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches.\n\nTl;dr"
#process_text(prompt)

def compuer_doctor():
    prompt = """Classify the following inquiry into one of the following: categories: [Pricing, Hardware Support, Software Support]
    inquiry: Hello, My computer is turning on but OS not loading giving bluescreen. I need help as soon as possible. Thank you.
    Classified category:"""
    print(prompt)
    process_text(prompt)

def baby_name_generator(number_of_names=5, gender="female"):
    prompt = f"""Generate a baby name in Turkish for a {gender} with top most used {number_of_names} names in during 2020 to 2030"""
    print(prompt)
    process_text(prompt)

baby_name_generator(10, "female")    