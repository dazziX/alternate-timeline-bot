# QUICK EXAMPLE ON GENERATING ALTERNATE TIMELINE FACTS

import fake.trivia as alt

day = alt.get_trivia() #generates an alternate timeline fact and a query(for finding images)

print(day['text']) #the text of the fact
print('-'*30)
print(day['query']) #the query

image = alt.generate_image(day['text'], day['query']) #generates the image

image['out'].save('output.png') #saves the image output
image['unsplash'].save('source.png') #saves the Unsplash source image
