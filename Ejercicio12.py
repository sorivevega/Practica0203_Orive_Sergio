#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input('Escribe una frase: ')
letra = input('Escribe una letra: ')
veces = 0
for x in frase:
    if x == letra:
        veces +=1
print(letra, 'aparece', veces, 'veces')