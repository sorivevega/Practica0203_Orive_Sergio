#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****
numero = int(input('Introduzca un numero: '))
for x in range(1, numero + 1):
    print('*' * x)