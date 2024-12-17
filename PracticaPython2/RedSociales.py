import Usuarios
import Publicaciones
class RedSocial:
    def __init__(self):
        self.listaUsuarios=[]
        self.listaPublicaciones=[]
    
    def registrar_usuario(self,id,nombre,email):
        
        nuevo_usuario = Usuarios.Usuario(id,nombre,email)
        
        self.listaUsuarios.append(nuevo_usuario)
        
        return nuevo_usuario
    
    def crear_publicacion(self,id_publicacion,contenido):
        
        nueva_publicacion = Publicaciones.Publicacion(id_publicacion,contenido)
        
        self.listaPublicaciones.append(nueva_publicacion)
        
        return nueva_publicacion
    
    def listar_usuarios(self):
        
        return self.listaUsuarios
    
    def listar_publicacion(self):
        
        return self.listaPublicaciones
    
    def ver_publicacion(self, id):
        
        for publicacion in self.listaPublicaciones:
            if publicacion.id_publicacion == id:
                return publicacion.ver_detalles()
        return "Publicación no encontrada"
        
        