import math
class FirstExercise:
    def __init__(self,number,chapter):
        self.number=number
        self.chapter=chapter
    def imprimirNumero(self):
        print(self.number)
    def imprimirChapter(self):
        print(self.chapter)
    
numeroYCapitulo = FirstExercise(6,"Clases y objetos")
numeroYCapitulo.imprimirNumero()
numeroYCapitulo.imprimirChapter()

class formulasYCalculos:
    def __init__(self,radio):
        self.radio=radio
    
    def calculos(self):
        area=(self.radio**2)*math.pi
        perimetro=(math.pi*2)*self.radio
        
        return area,perimetro
    
    def cambiarRadio(self,nuevoRadio):
        self.radio=nuevoRadio
        
radio1 = formulasYCalculos(10.5)
radio1.calculos()
area, perimetro = radio1.calculos()
print(round(area,2))
print(round(perimetro,2))
radio1.cambiarRadio(20.5)
print(radio1.radio)
radio1.calculos()
area, perimetro = radio1.calculos()
print(round(area,2))
print(round(perimetro,2))
