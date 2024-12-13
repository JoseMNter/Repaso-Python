from collections import Counter
lista = [1,1,2,2,3,3,3,4,5,6,7]

conteo = Counter(lista)

print(conteo)

frase = "Me llamo Jose y el perro no se llama Jose, pero el perro sigue ladrando cuando le llamo por su nombre"

palabras = frase.split(" ")

conteo_palabras = Counter(palabras)

print(conteo_palabras.most_common(2))

