import facebook
import fake.trivia as dt
from credentials import *

graph = facebook.GraphAPI(ACCESS_TOKEN)
trivia = dt.get_trivia()
print(trivia['text'])
print('-'*20)
print(trivia['query'])
img = dt.generate_image(trivia['text'],trivia['query'])
img['final'].save('output.png')
graph.put_photo(image=open('output.png', 'rb'))

