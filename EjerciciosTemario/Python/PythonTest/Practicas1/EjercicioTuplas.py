""" Para realizar este ejercicio crea una tupla con los siguientes valores: coche, motocicleta y camion """
tupla =("coche","motocicleta","camion")
""" Accede al primer y último elemento de la tupla e imprime sus valores """
elementos=str(tupla[0])+" "+str(tupla[-1])
print(elementos)
""" Crea otra tupla de forma distinta a la del inicio con los valores: perro, gato y naranja """
valor1="perro"
valor2="gato"
valor3="naranja"
nuevaTupla=(valor1,valor2,valor3)
""" Concatena las dos tuplas en una nueva con el nombre ‘tupla_concatenada’ """
tupla_concatenada = tupla+nuevaTupla
print(tupla_concatenada)
""" Cuenta el número de elementos de la tupla del punto 3 """
print("Cantidad de elementos: "+str(len(tupla_concatenada)))
""" Encuentra el índice del elemento perro dentro de ‘tupla_concatenada’ """
print(tupla_concatenada.index("perro"))
""" Desempaqueta ‘tupla_concatenada’ en las variables (por este orden) tp1, tp2, tp3 y el resto en tp4 """
tp1,tp2,tp3, *tp4 = tupla_concatenada
""" Imprime los valores de las variables (tp1 = coche, tp2 = motocicleta, tp3 = camon…) """
print(str(tp1)+", "+str(tp2)+", "+str(tp3)+" y los elementos restantes: "+str(tp4))
""" Añade un nuevo elemento a ‘tupla_concatenada’ """
nuevoElemento=("caracol",)
tupla_concatenada=tupla_concatenada+nuevoElemento
""" Muestra los elementos de ‘tupla_concatenada’ """
print(tupla_concatenada)