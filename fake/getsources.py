import requests
import time
d = list(range(1,32))
md = [(i,d) for i in range(1,13)]


with open('fake/trivias.txt', 'a') as f:
    for month,days in md:
        for day in days:
            t1 = time.time()
            text = requests.get(f'http://numbersapi.com/{str(month)}/{str(day)}/date').text
            fixed = ' '.join(text.split()[2:])
            f.write(fixed+'\n')
            print(' '.join(text.split()[0:2]))
            t2 = time.time()
            elapsed = t2 - t1
            print(f'Sleeping for {str(elapsed)} seconds...')
            time.sleep(elapsed)
