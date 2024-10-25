#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
palabra = input('Escribe una palabra: ')
palabra2 = palabra[::-1]
for letras in palabra2:
    print(letras)