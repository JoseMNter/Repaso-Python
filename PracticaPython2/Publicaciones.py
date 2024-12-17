class Publicacion:
    def __init__(self,id_publicacion,contenido):
        self.id_publicacion=id_publicacion
        self.contenido=contenido
        self.comentarios=[]
        
    def agregarComentario(self,texto):
        self.comentarios.append(texto)
        
    def ver_comentarios(self):
        return self.comentarios
    
    def ver_detalles(self):
        print(f"Contenido de la aplicación: {self.contenido}\nLista de comentarios:\n{self.comentarios}")
    
    
        