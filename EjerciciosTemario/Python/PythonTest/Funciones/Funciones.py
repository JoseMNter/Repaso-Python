""" Define una función llamada showAnimal que reciba dos argumentos name y n_legs e imprima esta información por pantalla. """

def showAnimal(name, n_legs):

    print(f"Nombre del animal: {name} y tiene {n_legs} patas.")
    
showAnimal("Gato",4)

""" Define una función que puede recibir cualquier número de argumentos e imprima cuántos argumentos ha recibido. """

def cuantosArgumentos(*args):
    print(len(args))

cuantosArgumentos(1,2,3,4,5,6,7)

""" Define una función que recibiendo dos números, devuelva la suma y la resta de ellos en una sola llamada. """

def sumaYresta(valor1,valor2):
    print(f"Suma de {valor1} y {valor2}: {valor1+valor2}")
    print(f"Resta entre {valor1} y {valor2}: {valor1-valor2}")

sumaYresta(10,8)

""" Define una función que recibiendo dos números devuelva la multiplicación. """

def multiplicacion(valor1,valor2):
    print(f"Multiplicación entre {valor1} y {valor2}: {valor1*valor2}")
    return valor1*valor2

multiplicacion(10,32)

""" Define una función que recibiendo dos números devuelva el módulo. """

def modulo(valor1,valor2):
    print(f"El módulo entre {valor1} y {valor2} es: {valor1%valor2}")
    return valor1%valor2

modulo(34,6)

""" Define una función que recibiendo una función del ejercicio 4 o ejercicio 5 y dos valores numéricos devuelva su resultado. """

def recibirFunciones(valor1,valor2):
    multiplicacion(valor1,valor2)

recibirFunciones(40,90)

""" Define una función que reciba el nombre y email de una persona. Si no recibe email, se asignará “Sin determinar”. La función debe imprimir el nombre y email de la persona. """

def datosDeUsuario(nombre, email=None):
    if email is None or email == "":
        email = "Sin determinar"
    
    print(f"Nombre de usuario: {nombre}")
    print(f"Email: {email}")

# Prueba de la función
datosDeUsuario("jose", "josemak87@hotmail.es")  # Con email
datosDeUsuario("ana")  # Sin email

""" Define una función que recibiendo un entero positivo, irá sumando este número a su anterior hasta llegar a 0 y devolverá el resultado final. """

def reciboEntero(valor):

    resultado=0

    while valor >=0:
        resultado += valor
        valor-=1

    return resultado

print(reciboEntero(5))