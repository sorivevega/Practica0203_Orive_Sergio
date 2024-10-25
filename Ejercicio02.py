#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
x = float(input('Introduce un numero: '))
y = float(input('Introduce un numero: '))
if y == 0:
    print('Error')
if y != 0:
    z = float(x // y)
    print(z)