class Vehicle:
    
    owner = "Nter"
    
    def __init__(self,nombre,velocidadMaxima,KM):
        self.nombre=nombre
        self.velocidadMaxima=velocidadMaxima
        self.KM=KM
        
    def agregarCapacidad(self,capacidad):
        print(f"La capacidad de {self.nombre} es de {capacidad}")

class Bus(Vehicle):
    def __init__(self, nombre, velocidadMaxima, KM):
        super().__init__(nombre, velocidadMaxima, KM)
    
    def agregarCapacidad(self,capacidad=50):
        self.capacidad=capacidad
        print(f"La capacidad de {self.nombre} es de {capacidad}")
        
    def calcularDistancia(self):
        if self.capacidad <= 50:
            raise ValueError("No se puede usar la capacidad por defecto para el cálculo de distancia, tampoco, una menor que la de por defecto.")
        distancia=self.capacidad*self.KM
        print(f"La distancia es de: {distancia}")
        return distancia
            
        
        
        

autobus = Bus("Majarron",150,50)
autobus.agregarCapacidad()

try:
    autobus.agregarCapacidad(60)
    distancia = autobus.calcularDistancia()
except ValueError as e:
    print(f"Error: {e}")

        