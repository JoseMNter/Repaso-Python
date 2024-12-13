""" Define una variable con un string con el valor “   Master Python”. """
cadenaDeTexto="    Master Python"
""" Muestra la longitud de la variable anterior. """
print(len(cadenaDeTexto))
""" Muestra el primer carácter del string. """
cadenaSinEspacios = cadenaDeTexto.strip()
print(cadenaSinEspacios[0])
""" Muestra el penúltimo carácter del string. """
longitudDeCadena = len(cadenaDeTexto)
print(cadenaDeTexto[longitudDeCadena-2])
""" Elimina los espacios iniciales del string. """
print(cadenaSinEspacios)
""" Muestra los caracteres en posiciones impares. """
print(cadenaSinEspacios[1::2])
""" Convierte todo el string en minúscula. """
print(cadenaSinEspacios.lower())
""" Separa el string por espacios en blanco. """
print(cadenaDeTexto.split(" "))
""" Reemplaza “python” por “JAVA”. """
print(cadenaDeTexto.replace("Python","JAVA").strip())
