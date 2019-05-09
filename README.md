# AlternateTimeline-Bot
The source code for the Facebook bot [AlternateTimeline-Bot](https://www.facebook.com/AlternateTimeline-Bot-1388202901322650/)
(ignore the "real" directory its unrelated)

# Dependencies
* [markovify](https://github.com/jsvine/markovify)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [requests](https://2.python-requests.org/en/master/)

# Quick Usage
If you want to generate alternate timeline facts on your own local machine, you can easily do that.  
(Note: You must have the "fake" directory in the directory that your script is in.)  
```python
# QUICK EXAMPLE ON GENERATING ALTERNATE TIMELINE FACTS
# THE "fake" DIRECTORY MUST BE IN THE SAME DIRECTORY WHERE THIS SCRIPT IS

import fake.trivia as alt

day = alt.get_trivia() #generates an alternate timeline fact and a query(for finding images)

print(day['text']) #the text of the fact
print('-'*30)
print(day['query']) #the query

image = alt.generate_image(day['text'], day['query']) #generates the image

image['out'].save('output.png') #saves the image output
image['unsplash'].save('source.png') #saves the Unsplash source image
```
Also, you can generate a fact with your own custom text and image query as well.  
(query keywords are separated by commas ",")  
Ex.  
```python
image = alt.generate_image("DONALD TRUMP IS GONE","Donald,Trump,Crab,Island")
```



