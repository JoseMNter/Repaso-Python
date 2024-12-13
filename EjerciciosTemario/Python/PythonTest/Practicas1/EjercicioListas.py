""" Añade “Word” al final de la lista. """
lista = [10,20,"Hello",20.5]
lista.append("Word")
print(lista)
""" Añade “Python” al principio de la lista. """
lista.insert(0,"Python")
print(lista)
""" Elimina el segundo valor de la lista. """
lista.pop(1)
print(lista)
""" Crea una segunda lista con los valores 20, 40, ‘Bye’ (utiliza una forma diferente que en el inicio) """
listaNueva=[]
valor1=20
valor2=40
valor3="Bye"
listaNueva=[valor1,valor2,valor3]
print(listaNueva)
""" Une las dos listas. """
lista.extend(listaNueva)
""" Muestra la lista final. """
print(lista)