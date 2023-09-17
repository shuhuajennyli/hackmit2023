import openai
import os
import requests
from PIL import Image
import random

openai.api_key = "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"
openai.Model.list()

'''
response = openai.Image.create(
    prompt = "create a painting of i hate life im so tired what is going on. don't have text in the painting",
    n=2,
    size="1024x1024",
    response_format="url"
)
url = response["data"][0]["url"]
data = requests.get(url).content
f = open('img.jpg','wb')
f.write(data)
f.close()
img = Image.open('img.jpg')
img.show()
'''


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


def generate(typ, num):
    if len(thoughtsHis) == 0:
        return "Enter a thought first!"

    if num > len(thoughtsHis):
        num = len(thoughtsHis)

    thoughts = ""
    for x in range(num):
        thoughts += thoughtsHis[x] + " "

    thoughtsLen = len(thoughts)
    if thoughtsLen < 250:
        lenPoem = "exactly 4 lines"
    elif thoughtsLen < 1000:
        lenPoem = "medium"
    else:
        lenPoem = ""
 
    inp = "Write a " + typ + " poem with these thoughts: " + thoughts + " As well, make it " + lenPoem
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
    img = Image.open('img.jpg')
    img.show()

    return completion.choices[0].message.content


while True:
    thoughts = input("Type generate, write away, or answer " + prompts[random.randrange(len(prompts))])
    if thoughts == "generate":
        typ = input("What type of poem would you like to generate? ")
        num = int(input("how many prev thoughts: "))
        print(generate(typ, num))

    else:
        thoughtsHis.insert(0, thoughts)