import Tareas,Usuarios
from datetime import datetime


class gestion:
    def __init__(self):
        self.listaTareas=[]
        self.listaUsuarios=[]
        self.tareasAsignadas=[]
        
    def agregarTarea(self,tarea_id,nombre_tarea,descrip_tarea,importancia):
    
        CantidadDeDificultades=[1,2,3]
        
        if importancia not in CantidadDeDificultades:
            
            print("La dificultad está entre 1 y 3")
            return
        
        else:
            
            nueva_tarea = Tareas.tarea(tarea_id,nombre_tarea,descrip_tarea,importancia)
            self.listaTareas.append(nueva_tarea)
        
        return nueva_tarea
    
    def agregarUsuario(self,id_usuario,nombre,departamento):
        
        nuevo_usuario = Usuarios.usuario(id_usuario,nombre,departamento)
        
        self.listaUsuarios.append(nuevo_usuario)
        
        return nuevo_usuario
    
    def listar_tareas(self):
        
        return self.listaTareas
    
    def listar_usuarios(self):
        
        return self.listaUsuarios
    
    def eliminar_tarea(self,id_tarea):
        
        for tarea in self.listaTareas:
            
            if tarea.id == id_tarea:
                
                self.listaTareas.remove(tarea)
                
        return "Eliminación completada satisfactoriamente.\n"
    
    def eliminar_usuario(self,id_usuario):
        
        for usuario in self.listaUsuarios:
            
            if usuario.id == id_usuario:
                
                self.listaTareas.remove(usuario)
                
        return "Eliminación completada satisfactoriamente.\n"
    
    def buscarUsuarioPorId(self,id_usuario):
        
        for usuario in self.listaUsuarios:
            
            if usuario.id == id_usuario:
                
                return usuario
            
            else:
                
                return "Usuario no encontrado.\n"
            
    
    def buscarTareaPorId(self,id_tarea):
        
        for tarea in self.listaTareas:
            
            if tarea.id_tarea == id_tarea:
                
                return tarea
                
        return "Tarea no encontrada.\n"
            
    
    def actualizarDepartamentoDelUsuario(self,id_usuario):
        
         for usuario in self.listaUsuarios:
            
            if usuario.id == id_usuario:
                
                nuevo_departamento = input("Introduce el nuevo departamento.")
                
                usuario.departamento = nuevo_departamento
                
                return "Departamento actualizado exitósamente.\n"
            
            else:
                
                return "Usuario no encontrado.\n"
            
    def actualizarTarea(self,id_tarea):
        
        for tarea in self.listaTareas:
            
            if tarea.id == id_tarea:
                
                try:
                    
                    opcion=int(input("Elige una opción:\n1) Cambiar nombre\n2) Cambiar descripción\n 3) Cambiar importancia"))
                    
                    match opcion:
                        
                        case 1:
                            
                            nuevo_nombre=input("Introduce el nuevo nombre de la tarea: ")
                            
                            print(f"Nombre cambiado de {tarea.nombre} a {nuevo_nombre}")
                            
                            tarea.nombre = nuevo_nombre
                            
                        case 2:
                            
                            nueva_descripcion=input("Introduce la nueva descripción de la tarea: ")
                            
                            print(f"Descripción antigua:\n{tarea.descripcion}\nDescripción nueva:\n{nueva_descripcion}")
                            
                            tarea.descripcion = nueva_descripcion
                            
                        case 3:
                            
                            while True:
                                
                                nueva_importancia=int(input("Mínimo 1, máximo 3"))
                                
                                if nueva_importancia <= 0 or nueva_importancia > 3:
                                    
                                    print("Por favor, introduce un valor correcto.")
                                
                                else:
                                    
                                    print("Se ha cambiado la importancia exitosamente.\n")
                                    
                                    tarea.importancia = nueva_importancia
                                    
                                    break
                        case _:
                            
                            print("Introduce una opción válida.")
                        
                except ValueError:
                    
                    print("Tienes que introducir un valor númerico para que funcione bien la aplicación")  
            
            else:
                
                return "Tarea no encontrada.\n"
    
    def asignarTarea(self, id_asignacion, tarea, usuario):
        fecha = datetime.now()
        
        asignacion = {
            "id_asignacion": id_asignacion,
            "tarea": tarea,
            "usuario": usuario,
            "fecha": fecha
        }
        
        self.tareasAsignadas.append(asignacion)

        
            
    
    
    