class Androide:
    def encendido(self):
        print("Estoy encendido") 
    def apagado(self):
        print("Estoy apagado")
class Prototipo(Androide):
    def encendido(self):
        print("Me he encendido pero de manera diferente.")
    
droide1=Androide()
droide2=Prototipo()

droide1.encendido()
droide2.apagado()
droide2.encendido()

