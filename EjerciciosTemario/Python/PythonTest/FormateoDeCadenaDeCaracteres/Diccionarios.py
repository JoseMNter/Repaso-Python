listaDeCoches = [
    {
        "nombre":"Citroen",
        "kilometros":200,
        "deposito":150,
        "modelo:":"ABC120",
        "color":"Blanco"
    },
    {
        "nombre":"Toyota",
        "kilometros":100,
        "deposito":200,
        "modelo:":"DFG2783",
        "color":"Rojo"
    }
]

coche = {
    "nombre":"Volvo",
        "kilometros":240,
        "deposito":100,
        "modelo:":"JHKJHD7",
        "color":""
}

print(listaDeCoches[0].get("nombre"))
listaDeCoches.append(coche)
print(listaDeCoches[2])

if(listaDeCoches[2].get("color")==""):
    listaDeCoches[2]["color"] = "Blanco"

print(listaDeCoches[2])


""" https://www.w3schools.com/python/ref_dictionary_setdefault.asp """

