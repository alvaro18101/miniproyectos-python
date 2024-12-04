import json
import random

path = 'conectores.json'

# Reading .json
with open (path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Number of words
length = 0
for i in data:
    for j in data[i]:
        length += 1

# Word of day:
random_number = random.randint(1,length)
print(f'Palabra de hoy: N° {random_number}')

k = 0
for i in data:
    for j in data[i]:
        k +=1
        if k == random_number:
            word_of_day = data[i][j]
            break
    if k == random_number:
        break

print(f'The word of the day is: {j}')
translation = input('Input the translation: ')
while translation.lower() != data[i][j].lower():
    if translation.lower() == 'give up':
        break
    print('Wrong!')
    translation = input('Input the translation: ')

if translation.lower() == data[i][j].lower():
    print('Nice!')
    print(f'{i}: {j}: {data[i][j]}')
elif translation.lower() == 'give up':
    print(f'{i}: {j}: {data[i][j]}')