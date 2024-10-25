#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
contraseña = 'Python'
password = input('Introduce la contraseña: ')
while password != contraseña:
    password = input('Introduce la contraseña: ')