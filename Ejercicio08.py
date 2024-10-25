#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
x = 10
z = range(1, 10)
for y in range(1, x + 1 ):
    for z in range(1, x + 1):
        print(y, '*', z, '=', str(y * z))