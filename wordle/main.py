from colorama import init, Fore, Back, Style
# import scraping de palabras válidas y palabra elegida
init()

chosen_word = 'albañil'
dictionary = ('albañil', 'mesa', 'camaras', 'alberto')


import json
import random

with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)  # Cargar el contenido del archivo como un diccionario
datos_a = datos['a']
random_number = random.randint(0,len(datos_a)-1)

chosen_word = datos_a[random_number]
dictionary = datos_a


counter0 = {}

for i in chosen_word:
    if i in counter0:
        counter0[i] += 1
    else:
        counter0[i] = 1

mi_color_personalizado = "\033[38;2;255;165;0m"  # Naranja
fondo_personalizado = "\033[48;2;0;80;0m"      # Gris oscuro
fondo_personalizado2 = "\033[48;2;95;95;0m"      # Gris oscuro

def greentLetter(letter):
    return fondo_personalizado +  Style.BRIGHT +letter + Back.RESET + Style.RESET_ALL

def yellowLetter(letter):
    return fondo_personalizado2 + letter + Back.RESET

def printInfo(string):
    print(Back.BLUE + Fore.WHITE + Style.BRIGHT + '   ' + string + '   ' + Back.RESET + Fore.RESET + Style.RESET_ALL)


def showBoard(array):
    # for i in range(len(chosen_word)):
    #     print(i, end=' ')
    # print('■ ■ ■ ■ ■ ■ ■')
    print('_ _ _ _ _ _ _')

isInDictionary = lambda word_inputted: True if word_inputted in dictionary else False


def checkLetter(split_word):
    word = ''
    counter = {}
    for i in range(len(split_word)):
        if split_word[i] in chosen_word:
            if split_word[i] in counter:
                counter[split_word[i]] += 1
            else:
                counter[split_word[i]] = 1

            if split_word[i] == chosen_word[i]:
                word += greentLetter(split_word[i].upper()) + ' '
            if split_word[i] != chosen_word[i]:
                if counter[split_word[i]] <= counter0[split_word[i]]:
                    word += yellowLetter(split_word[i].upper()) + ' '
                else:
                    word += split_word[i].upper() + ' '
        else:
            word += '_ '
    return word


board = len(chosen_word)*'_ '
print(board)
print()
# board = showBoard('instrucciones inciales de la palabra')
attempts = 6
for i in range(attempts, 0, -1):
    is_won = False
    print('Intento:', i)
    print()
    # showBoard('__')
    print()
    word_inputted = input('-> ').lower()

    while True:
        if len(word_inputted) == len(chosen_word) and isInDictionary(word_inputted) == True:
            break
        if len(word_inputted) != len(chosen_word):
            printInfo(f'La palabra debe tener {len(chosen_word)} caracteres')
        if isInDictionary(word_inputted) == False:
            printInfo('La palabra no existe')
        word_inputted = input('-> ').lower()

    if word_inputted == chosen_word:
        is_won = True
        break

    # while len(word_input) != len(chosen_word) or isInDictionary(word_input) == False:
    #     if len(word_input) != len(chosen_word):
    #         printInfo(f'La palabra debe tener {len(chosen_word)} caracteres')
    #         word_inputted = input('->')

    #     if isInDictionary(word_inputted) == False:
    #         printInfo('La palabra no existe')
    #         word_input = input('->')
    
    split_word = list(word_inputted)
    palabra = checkLetter(split_word)

    print(palabra)

if is_won:
    print(checkLetter(list(word_inputted)))
    print('Palabra acertada')
else:
    print('Perdiste')
    print(f'La palabra era {chosen_word.upper()}')