import openai
import os
import requests
from PIL import Image
import random

openai.api_key = ""
openai.Model.list()

prompts = ["How are you feeling right now, in this moment? ", 
    "Can you describe a recent situation that made you feel really happy or content? ", 
    "What's been on your mind lately that has been causing you stress or anxiety? ", 
    "What's been on your mind lately that has been causing you stress or anxiety? ", 
    "Is there a particular memory from your past that still evokes strong emotions when you think about it? ",
    "What are some activities or hobbies that genuinely make you feel excited or passionate? ",
    "Can you recall a time when you felt proud of yourself? What did you achieve or overcome? ",
    "Have you experienced any moments of sadness or grief recently? What's been causing those emotions? ",
    "Describe a time when you felt a deep sense of gratitude or appreciation for something or someone. ",
    "Are there any emotions you find challenging to express or confront? Why do you think that is? ",
    "Do you notice any recurring emotional patterns or themes in your life? ",
    "How do you typically cope with difficult emotions? Are there healthy strategies that work for you? "
    "Are there any emotional goals or personal growth areas you'd like to explore or work on? ",
    "What kind of music, art, or literature resonates with your emotions? Can you give examples? ",
    "Do you find it easier to express your emotions verbally, through writing, or through other creative outlets? ",
    "How do you think your emotional state affects your relationships with others? "]

thoughtsHis = []

def generateGPT(text_input, poem_spec, lenPoem):

    if len(text_input) == 0:
        return "Enter a thought first!"

    inp = "Write a " + poem_spec + " poem with these thoughts: " + text_input + " As well, make it " + lenPoem
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": inp}])

    response = openai.Image.create(
        prompt = completion.choices[0].message.content,
        n=2,
        size="1024x1024",
        response_format="url"
        )
    url = response["data"][0]["url"]
    data = requests.get(url).content
    f = open('img.jpg','wb')
    f.write(data)
    f.close()
    img = 'img.jpg'

    return completion.choices[0].message.content, url