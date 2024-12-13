""" Esto es una lista con distintos tipos de datos: """
listaDePrueba = [1,2.0,"Hola",True,[1,2]]
""" Esto es una lista vacia """
listaVacia=[]
""" Tercer elemento desde el final """
listaDeNumeros=[1,2,3,4,5,6,7,8,9,10]
print(listaDeNumeros[-3])
print(listaDeNumeros[:2])
sublista_entre_x_y = listaDeNumeros[0:5]
print(sublista_entre_x_y)
sublista_desde_x_de_dos_en_dos = listaDeNumeros[0::2]
print(sublista_desde_x_de_dos_en_dos)
#%%
lista_de_objetos=["Objeto1","Objeto2","Objeto3","Objeto4","Objeto5"]
IndiceDeObjeto5 = lista_de_objetos.index("Objeto5")
print(IndiceDeObjeto5)

lista_de_frutas=["Manzana","Pera","Kiwi","Naranja","Melón"]
buscar_Kiwi=lista_de_frutas.index("Kiwi")
print(lista_de_frutas[buscar_Kiwi])
lista_de_frutas.pop(buscar_Kiwi)
print(lista_de_frutas)
lista_de_frutas.append("Kiwi")
print(lista_de_frutas)
# %%
listaDeNumeros=[1,2,3,4,5]
mi_tupla = (listaDeNumeros[2],listaDeNumeros[1])
print("Suma total de los numeros: "+str(sum(mi_tupla)))
print(f"Suma total de los numeros: {sum(mi_tupla)}")

# %%
