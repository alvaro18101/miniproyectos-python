import json
import random

with open("datos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)  # Cargar el contenido del archivo como un diccionario