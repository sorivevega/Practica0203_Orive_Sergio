#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contraseña = 'Python'
x = (input('Introduzca su contraseña: '))
if x == contraseña.lower():
    print('Correcto')
elif x != contraseña.lower():
    print('Error')