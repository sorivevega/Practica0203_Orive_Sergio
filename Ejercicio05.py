#Los alumnos de Hogwarts se han dividido en dos casas, Gryffindor y Slytherin, de acuerdo al sexo y el nombre. Gryffindor está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y Slytheryn por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
sexo = input('¿Eres Hombre o Mujer?: ')
name = input('¿Como te llamas?: ')
if sexo.lower() == 'mujer':
    if name[0].lower() < 'm':
        print('Perteneces a Gryffindor')
    else:
        print('Perteneces a Slytherin')
elif sexo.lower() == 'hombre':
    if name[0].lower() > 'n':
        print('Perteneces a Gryffindor')
    else:
        print('Perteneces a Slytherin')