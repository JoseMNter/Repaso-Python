class NombreDeClase:
    """ Esto es un ejemplo """
    ejemplo_valor = "Hola"
    
    def __init__(self, parametro1, parametro2):
        
        self.parametro1 = parametro1
        self.parametro2 = parametro2
        
    def metodo_de_Clase(self):
        
        return self.parametro1 + self.parametro2
    

un_ejemplo = NombreDeClase(20,30)
print(un_ejemplo.metodo_de_Clase())
print(un_ejemplo.parametro2)