from collections import defaultdict
""" Para realizar este ejercicio tienes un diccionario con las claves: 
coche, motocicleta, camión y los valores: 10, 20 y 30 respectivamente. """

""" Define el diccionario usando dict(). """
lista = dict([
    ("coche",10),
    ("motocicleta",20),
    ("camión",30)
])
""" Define el diccionario usando { }. """
lista2 = {
    "coche":10,
    "motocicleta":20,
    "camión":30
}
""" Muestra los valores del diccionario. """
print(str(lista)+"\n"+str(lista2))

""" Muestra las claves del diccionario. """
print(lista.keys())
""" Muestra el valor de coche. """
print(lista.get("coche"))
""" Añade al diccionario avión con valor 100."""
lista.update({"avión":100})
""" Muestra los elementos del diccionario.  """
print(lista)
