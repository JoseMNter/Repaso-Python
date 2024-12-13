from collections import defaultdict

frutas = [
    ("manzana",2),
    ("pera",3),
    ("manzana",1)
]

conteo_de_frutas = defaultdict(int)

for fruta, cantidad in frutas:
    conteo_de_frutas[fruta] +=cantidad

print(dict(conteo_de_frutas))