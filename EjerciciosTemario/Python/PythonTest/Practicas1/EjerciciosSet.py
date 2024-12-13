""" Define un conjunto con los valores coche, motocicleta, bicicleta. """
ListaDeObjetosSet={"coche","motocicleta","bicicleta"}
print(ListaDeObjetosSet)
""" Añade avión al conjunto. """
ListaDeObjetosSet.add("avión")
print(ListaDeObjetosSet)
""" Elimina coche del conjunto. """
ListaDeObjetosSet.discard("coche")
print(ListaDeObjetosSet)
""" Crea otro conjunto con los valores avión, coche, tractor (utiliza una forma diferente que en el punto 1). """
valor1="avión"
valor2="coche"
valor3="tractor"
listaNueva={valor1,valor2,valor3}
print(listaNueva)
""" Crea otro conjunto con los valores que se repitan en los conjuntos anteriores. """
listaRepetida=ListaDeObjetosSet.intersection(listaNueva)
print(listaRepetida)
""" Muestra un conjunto con todos los valores que pertenecen al conjunto creado en el punto 1 y punto 4 """
listaDeTodosLosValores=ListaDeObjetosSet.union(listaNueva)
print(listaDeTodosLosValores)