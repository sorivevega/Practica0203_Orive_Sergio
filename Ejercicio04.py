#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
edad = int(input('Introduzca su edad: '))
if edad < 16:
    print('No debe tributar') 
elif edad >= 16:
    dinero = float(input('Introduzca sus ingresos: '))
    if dinero < 1000:
        print('No debe tributar')
    elif dinero >= 1000:
        print('Debe tributar')