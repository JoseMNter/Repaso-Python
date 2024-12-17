class Usuario:
    def __init__(self, id,nombre,email):
        self.id=id
        self.nombre=nombre
        self.email=email
        self.publicaciones=[]
    
    def crear_publicacion(self,id_publicacion):
        self.publicaciones.append(id_publicacion)
        
    def ver_publicaciones(self):
        return self.publicaciones
    
        