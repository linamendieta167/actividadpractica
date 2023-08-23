#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def contar_palabras(text):
   
    text = text.split()
    palabras = {}
    for i in text:
        if i in palabras:
            palabras[i] += 1
        else:
            palabras[i] = 1
    return palabras

def mas_repetido(palabras):
    max_palabra = ''
    max_freq = 0
    for palabra, freq in palabras.items():
        if freq > max_freq:
            max_palabra = palabra
            max_freq = freq
    return max_palabra, max_freq

text = input("ingrese una cadena de caracteres: ")

print(f" cadena de caracteres a diccionario con el numero de veces repetido: {contar_palabras(text)}")
print(f" palabra mas repetida: {mas_repetido(contar_palabras(text))}")
