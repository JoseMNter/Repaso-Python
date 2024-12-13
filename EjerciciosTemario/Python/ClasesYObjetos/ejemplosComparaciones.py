class Droide:
    def __init__(self, nombre, serial):
        
        self.nombre = nombre
        self.serial = serial
        
    def __eq__(self, droide):
        
            return self.nombre == droide.nombre
    

droide1 = Droide("Nombre1",13287231132)
droide2 = Droide("Nombre1",13287231132)

print(droide1 == droide2)
print(droide2.serial == droide1.serial)

if droide1==droide2:
    print("Muy bien")
else:
    print("No")