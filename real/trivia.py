import requests
from datetime import date
from PIL import Image,ImageDraw,ImageFont,ImageOps
import random
from io import BytesIO
import re
import textwrap


def get_trivia(month: int=None,day: int=None):
    if not month or not day:
        now = date.today()
        month = now.month
        day = now.day
    trivia_text = requests.get(f'http://numbersapi.com/{str(month)}/{str(day)}/date').text
    query = make_query(trivia_text)
    return {'text':trivia_text,'query':query}


def make_query(text):
    query = ','.join([re.sub('[!?\"\',.]','',word) for word in text.split()[1:] if word[0].isupper()])
    if query == '':
        query = ','.join([re.sub('[!?\"\',.]','',word) for word in text.split()])
    return query

    
def generate_image(trivia, query):
    r = requests.get(f'https://source.unsplash.com/featured/?{query}')
    raw = r.content
    im = Image.open(BytesIO(raw))
    #width, height = im.size
    new = ImageOps.fit(im, (500,500), Image.LANCZOS, 0.0, (0.5,0.5))
    black_box = Image.new('RGB',(500,700),(10,0,0))
    black_box.paste(new, (0,0))
    final = add_text(trivia, black_box)
    return {'final':final,'old':im,'new':new}


def add_text(text,img):
    width,height = img.size
    lines = textwrap.wrap(text, width=42)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('times-new-roman.ttf',25)
    space = 0
    for line in lines:
        fw,fh = font.getsize(line)
        draw.text(((width - fw) // 2, 515 + space), line, font=font, fill=(255,255,255))
        space += fh + 4
        
    return img



if __name__ == '__main__':
    trivia = get_trivia()
    print(trivia['text'])
    print('-'*20)
    print(trivia['query'])
    img = generate_image(trivia['text'],trivia['query'])
    img['final'].save('final.png')

