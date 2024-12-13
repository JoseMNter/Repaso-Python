a = 10

b = 100

""" Defina una estructura de control que imprima por pantalla “Es igual a 10” si a es igual a 10 y si no
imprima “Es diferente de 10”.

Defina una estructura de control que imprima “Todos son igual a 10” si a y b son iguales a 10; si no
imprima “Solo a es igual a 10” si a es igual a 10; si no imprima “B es igual a 10” si b es igual a 10; si no
imprima “Ninguno es igual a 10”.

Defina una estructura de control que imprima “A y B son impares” si tanto a como b son impares; si no
imprima “A y B no son impares”. """

if a==10:
    print(f"a es igual a 10")
else:
    print(f"a es diferente a 10")

if a==10 and b ==10:
    print(f"Tanto a y b son iguales a 10")
elif a==10 and b!=10:
    print(f"a es igual a 10 pero b no")
elif a!=10 and b==10:
    print(f"a no es igual a 10 pero b sí")
else:
    print("Ninguno es igual a 10")

if a%2==0 and b%2==0:
    print("A y B son pares.")
else:
    print("A Y B son impares")

""" Asigna un valor a la variable i.

Defina una estructura de control que solo imprima i una vez.

Defina una estructura de control que imprima i solo si el valor de i es par.

Asigna i el valor 0. Crea una estructura de control que vaya incrementando i mientras i sea menor de 10.
Comprueba si el valor de i es 6 e imprime “Ejecución terminada” y finaliza el bucle. """

i=5

while i == 5:
    print(i)
    i+=1

j=0

while j<10:
    j+=1
    if j%2==0:
        print(j)
if j<=10:
    print(f"Se ha finalizado el bucle porque j ha llegado a {j}")


a = ['Hello',"World"]

b = ['Python',3.9]

c = "HelloWordPython"

""" Recorre todos los caracteres de c e imprímelos por pantalla.

Muestra todos los valores de a.

Muestra cada valor de a y b mostrando cada elemento de a con el de la misma posición de b sin utilizar
los índices de posición.

Muestra en cada iteración el valor y su índice para los elementos de b. """

for i in range(len(c)):
    print(c[i])

for valor in a:
    print(valor)

for valor_a, valor_b in zip(a,b):
    print(valor_a, valor_b)

for indice, valor_b in enumerate(b):
    print(indice,valor_b)


""" Crea una lista con los números del uno al 10 elevados al cuadrado

Crea una lista con los números pares del 1 al 20

Dada una lista de palabras crea una nueva lista con todas las palabras en mayúsculas

Dada una lista de números crear una nueva lista en la que se dupliquen los números impares

Dada una lista de palabras crea una lista con la segunda letra de cada palabra

Dada una lista de listas crea una lista con los elementos de todas las listas """

listaDeNumerosElevadosAlCuadrado=[1,2,3,4,5,6,7,8,9,10]

cuadrados=map(lambda x: x**2,listaDeNumerosElevadosAlCuadrado)
print(list(cuadrados))

listaDelUnoAlVeinte=[]

for i in range(21):
    if i%2==0:
        listaDelUnoAlVeinte.append(i)
print(listaDelUnoAlVeinte)


listasPalabras=["hola","nose","jaja","prueba"]
listaNuevaTransformada=[]

for palabra in listasPalabras:

    listaNuevaTransformada.append(palabra.upper())

print(listaNuevaTransformada)

mayusculas = map(lambda x: x.upper(), listasPalabras)
print(list(mayusculas))


listaDeNumeros=[1,2,3,4,5,6,7,8,9,10,11]

nuevaListaDuplicadaImpares=[]

for numero in listaDeNumeros:
    if numero%2!=0:
        nuevaListaDuplicadaImpares.append(str(numero)+" Duplicado: "+str(numero))
print(nuevaListaDuplicadaImpares)

listaDeLetras=[]

for palabra in listasPalabras:
    listaDeLetras.append(palabra[1])
print(listaDeLetras)
