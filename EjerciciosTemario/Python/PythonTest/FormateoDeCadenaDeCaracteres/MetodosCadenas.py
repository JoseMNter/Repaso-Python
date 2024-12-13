cadenaDeTexto = "Hola me llamo Jose"
longitudDeCadena = len(cadenaDeTexto)

listaDePalabras = cadenaDeTexto.split(" ")

print(f"La longitud de la cadena es: {longitudDeCadena}")
print(f"Vamos a separar las palabras de la cadena: {listaDePalabras}")
print("A continuación, se unen: ")
listaUnidadDeNuevo = " ".join(listaDePalabras)
print(listaUnidadDeNuevo)

print(f'Devuelve True si la listaDePalabras son todas letras: {cadenaDeTexto.isalpha()}')

