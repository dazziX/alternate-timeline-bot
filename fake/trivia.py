import requests
from datetime import date
from PIL import Image,ImageDraw,ImageFont,ImageOps
import random
from io import BytesIO
import re
import textwrap
import markovify



def get_trivia(month: int=None,day: int=None):
    if not month or not day:
        now = date.today()
        month = now.month
        day = now.day
        md_str = now.strftime(f'%B {day}')
    else:
        md_str = date(1900, month, day).strftime('%B %d')

    with open('fake/trivias.txt', encoding='utf-8') as f:
        model = markovify.NewlineText(f.read())
    markov_text = model.make_sentence(tries=50)
    trivia_text = f'{md_str} {markov_text}'
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
    #black_box = Image.new('RGB',(500,700),(10,0,0))
    #black_box.paste(new, (0,0))
    final = add_text(trivia, new)
    return {'out':final,'unsplash':im}


def add_text(text,img):
    width,height = img.size
    lines = textwrap.wrap(text, width=42)
    font = ImageFont.truetype('fake/times-new-roman.ttf',25)
    text_height = 42
    for line in lines:
        fw,fh = font.getsize(line)
        text_height += fh + 4

    text_box = Image.new('RGB',(500,height + text_height),(10,0,0))
    text_box.paste(img, (0,0))
    draw = ImageDraw.Draw(text_box)

    text_height = 0
    for line in lines:
        fw,fh = font.getsize(line)
        draw.text(((width - fw) // 2, 520 + text_height), line, font=font, fill=(255,255,255))
        text_height += fh + 4
        
    return text_box



if __name__ == '__main__':
    trivia = get_trivia()
    print(trivia['text'])
    print('-'*20)
    print(trivia['query'])
    img = generate_image(trivia['text'],trivia['query'])
    img['out'].save('out.png')
    
    
