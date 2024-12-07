import random
import requests
from bs4 import BeautifulSoup
import json

letters = 'abcdefghijklmnñstuvwxyz'
random_number = random.randint(0, len(letters)-1)
# url = 'https://dle.rae.es/' + letters[random_number] + '?m=33'

# url = 'https://www.listapalabras.com/palabras-con-A-lista-completa.php'
url = 'https://www.listapalabras.com/palabras-con.php?letra=A&total=s'
# url2 = 'https://www.listapalabras.com/palabras-con-A-lista-completa.php'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

dictionary = {}

# for letter in letters:
request_obtained = requests.get(url, headers=headers)
html_obtained = request_obtained.text
soup = BeautifulSoup(html_obtained, 'html.parser')

words = soup.find_all('a', {'id': 'palabra_resultado'})
words_array = []
for i in words:
    words_array.append(i.text[:-1])

dictionary['a'] = words_array

# Corrigiendo detalles
words_array.remove('a-')

with open("datos.json", "w", encoding="utf-8") as book:
    json.dump(dictionary, book, indent=4, ensure_ascii=False)