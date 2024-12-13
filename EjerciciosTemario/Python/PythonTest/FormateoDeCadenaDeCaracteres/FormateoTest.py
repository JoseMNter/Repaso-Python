first_name= "Jose"
last_name= "Manuel"
age = 38
height = 1.85555

formated_str = "Hola mi nombre es %s %s tengo %d años y mido %.2f cm"%(first_name, last_name, age, height)
print(formated_str)

formated_str2= 'Hola mi nombre es {} {} tengo {} años y mido {:.2f} cm'.format(first_name, last_name, age, height)
print(formated_str2)

formated_str3 = f'Hola mi nombre es {first_name} {last_name} tengo {age} años y mido {height:.2f} cm'
print(formated_str3)

""" Se puede usar F-strings para devolver resultados según una condición """

print('')
print('')
print('')

num1=10
num2=20

nombre="Antonio"
edad=27

print(f"Es num1 mayor que num2? {True if num1>num2 else False}")

print(f"{nombre=},{edad=}")

nombreYApellidos = "Jose Manuel de la Cruz Morente"

nombreSolo = nombreYApellidos[:4]
primerApellidos = nombreYApellidos[5:-19]
print(nombreSolo)
print(primerApellidos)



