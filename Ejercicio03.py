#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
x = input('Introduzca un numero: ')
y = int(x)
if(y % 2 == 0):
    print('Par')
elif(y % 2 != 0):
    print('Impar')