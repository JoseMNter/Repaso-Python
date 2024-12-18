import json, csv, Gestion, Tareas, Usuarios, colorama
from datetime import datetime

gestionNter = Gestion.gestion()

def main():
    
    print("Bienvenido a la aplicación de gestión de tareas y usuarios de Nter. Tiene disponible estas opciones:\n")
    
    while True:
        
        try:
            
            opcionMenu = int(input("1) Gestión de usuarios\n2) Gestión de tareas\n3) Salir\n"))

            match opcionMenu:
                    
                    case 1:
                        
                        try:
                            
                            print("Accedido a la gestión de usuarios. Tiene disponible estas opciones:\n")
                            opcionGestionU = int(input("1) Registrar usuario\n2) Asignar tarea a un usuario\n3) Consultar tareas asignadas de un usuario\n4) Listar todos los usuarios registrados\n5) Buscar un usuario por ID\n6) Eliminar un usuario por ID\n7) Cambiar de departamento a un usuario\n8) Volver atrás\n"))
                            
                            match opcionGestionU:
                                
                                case 1:
                                    
                                    id_nueva=int(input("Introduce la nueva ID: "))
                                    
                                    for usuario in gestionNter.listaUsuarios:
                                        
                                        if usuario.id == id_nueva:
                                            
                                            print("Ya existe un usuario registrado con esa ID.")
                                            
                                        else:
                                            
                                            nuevo_nombre = input("Introduce el nombre de usuario: ")
                                            nuevo_departamento = input("Introduce el departamento que pertenece: ")

                                            gestionNter.agregarUsuario(id_nueva,nuevo_nombre,nuevo_departamento)
                                            
                                            print(f"Se ha registrado un nuevo usuario a nombre de: {nuevo_nombre} con ID: {id_nueva}")
                                
                                case 2:
                                    
                                    print("---Lista de tareas registradas---\n")
                                    print(gestionNter.listaTareas)
                                    print("\n"*2)
                                    
                                    idDelUsuario = int(input("Introduce la ID del usuario al que le vamos a asignar la tarea: "))
                                    
                                    for usuario in gestionNter.listaUsuarios:
                                        
                                        if usuario.id == idDelUsuario:
                                            
                                            usuario_encontrado = usuario
                                            break
                                            
                                        else:
                                            
                                            print("No se ha encontrado el usuario por ID")
                                            
                                    idDeLaTarea = int(input(f"Introduce la ID de la tarea al que le vamos a asignar a {usuario_encontrado.nombre}\n"))
                                    
                                    for tarea in gestionNter.listaTareas:
                                        
                                        if tarea.id == idDeLaTarea:
                                            
                                            tarea_Encontrada = tarea
                                            break
                                        
                                        else:
                                            
                                            print("ID de la tarea no existe.")
                                            
                                    idAsignacion = int(input("Introduce el identificador de la signacion"))
                                    
                                    for asignacion in gestionNter.tareasAsignadas:
                                        
                                        if asignacion.id == idAsignacion:
                                            
                                            print("El identificador de la asignación ya existe.")
                                            break
                                            
                                        else:
                                            
                                            gestionNter.asignarTarea(idAsignacion,tarea_Encontrada,usuario_encontrado)
                                            fecha_asignacion = asignacion["fecha"].strftime("%Y-%m-%d %H:%M:%S")
                                            print(f"La tarea a nombre de {tarea_Encontrada.nombre} se le ha asignado a {usuario_encontrado.nombre} a fecha de {fecha_asignacion}")
                                            break
                                            
                                            
                                case 3:
                                    
                                    listaDeTareasAsignadas=[]
                                    
                                    idDelUsuarioAbuscar = int(input("Introduce la ID del usuario para consultar sus tareas asignadas."))
                                    
                                    for asignacion in gestionNter.tareasAsignadas:
                                        
                                        if asignacion["usuario"].id_usuario == idDelUsuarioAbuscar:
                                            
                                            listaDeTareasAsignadas.append(asignacion["tarea"])
                                            
                                        if listaDeTareasAsignadas:  
                                            print(f"Las tareas asignadas al usuario con ID {idDelUsuarioAbuscar} son: ")
                                            for tarea in listaDeTareasAsignadas:
                                                print(f"ID: {tarea.id_tarea} - {tarea.nombre}")  
                                        else:
                                            print("No se encontraron tareas asignadas para el usuario con esa ID.")
                                
                                case 4:
                                    
                                    print("---Lista de usuarios registrados---\n")
                                    gestionNter.listar_usuarios()
                                    
                                case 5:
                                    
                                    idABuscar = int(input("Introduce la ID a buscar: "))
                                    
                                    print(gestionNter.buscarUsuarioPorId(idABuscar))
                                    
                                case 6:
                                    
                                    idABuscar = int(input("Introduce la ID a buscar para su eliminación: "))
                                    
                                    print(f"Se va a eliminar el usuario: \n{gestionNter.buscarUsuarioPorId(idABuscar)}")
                                    
                                    gestionNter.eliminar_usuario(idABuscar)
                                    
                                case 7:
                                    
                                    idAbuscar=int(input("Vamos a cambiar de departamento a un usuario, por favor, introduce la ID del usuario que vamos a actualizar: "))
                                    
                                    for usuario in gestionNter.listaUsuarios:
                                        
                                        if usuario.id_usuario == idABuscar:
                                            
                                            nuevo_departamento = input("Introduce el nuevo departamento: ")
                                            
                                            usuario.departamento = nuevo_departamento
                                            
                                            print("Departamento cambiado exitosamente.")
                                            
                                            break
                                            
                                        else:
                                            
                                            print("No existe el usuario.")
                                
                                case 8:
                                    
                                    print("Volviendo..")
                                    
                                    break
                                
                                case _:
                                    
                                    print("Introduce una opción correcta.")
                                
                                
                        except ValueError:
                            
                            print("Introduce un valor númerico.")
                            
                    case 2:
                        
                        try:
                            
                            print("Accedido a la gestión de tareas. Tiene disponible estas opciones:\n")
                            opcionGestionT = int(input("1) Agregar tarea\n 2) Listar todas las tareas registradas\n3) Buscar tarea por ID\n4) Eliminar una tarea\n5) Volver atrás\n"))
                            
                            try:
                                
                                match opcionGestionT:
                                    
                                    case 1:
                                        id_tarea = int(input("Introduce la ID de la nueva tarea: "))
    
                                        
                                        tarea_encontrada = gestionNter.buscarTareaPorId(id_tarea)
    
    
                                        if tarea_encontrada != "Tarea no encontrada.\n":
                                            print(f"Ya existe una tarea con la ID {id_tarea}: {tarea_encontrada.nombre}")
                                        else:
        
                                            nombre_tarea = input("Introduce el nombre de la nueva tarea: ")
                                            descripcion_tarea = input("Introduce la descripción de la nueva tarea: ")
        
       
                                            nueva_tarea = gestionNter.agregarTarea(id_tarea, nombre_tarea, descripcion_tarea,3)
        
       
                                            gestionNter.listaTareas.append(nueva_tarea)
        
                                            print(f"Se ha creado una nueva tarea con ID {id_tarea}, nombre: {nombre_tarea}.")
                                    
                                    case 2:
                                        
                                        print("---Lista de tareas registradas---\n")
                                        print(gestionNter.listar_tareas())
                                        
                                    case 3:
                                        
                                        id_tarea = int(input("Introduce la ID a buscar: "))
                                        
                                        tareaEncontrada=gestionNter.buscarTareaPorId(id_tarea)
                                        
                                        print(tareaEncontrada)
                                        
                                    case 4:
                                        
                                        id_tarea = int(input("Introduce la ID a eliminar: "))

                                        tareaEncontrada = gestionNter.buscarTareaPorId(id_tarea)


                                        if tareaEncontrada == "Tarea no encontrada.\n":
                                            print(tareaEncontrada)
                                        else:
    
                                            for tarea_asignada in gestionNter.tareasAsignadas[:]:  
                                                if tarea_asignada["tarea"].id == tareaEncontrada.id:  
                                                    gestionNter.tareasAsignadas.remove(tarea_asignada)  

    
                                            gestionNter.listaTareas = [t for t in gestionNter.listaTareas if t.id != tareaEncontrada.id]

                                            print(f"Tarea con ID {id_tarea} eliminada correctamente.")
                                    
                                    case 5:
                                        
                                        print("Volviendo..")
                                        break
                                    
                                    case _:
                                        
                                        print("Introduce un opción correcta")
                                        
                            except ValueError:
                                
                                print("Introduce un valor númerico")
                        
                            
                        except ValueError:
                            
                            print("Introduce un valor númerico")
                            
                    case 3:
                        
                        print("Saliendo de la aplicación")
                        break
                    
                    case _:
                        
                        print("Introduce una opción correcta.")
                        
        except ValueError:
            
            print("Introduce un valor númerico.")
                        
                        
                      
main()
                                            
                                    
                                    
                                            
                                            
                                    
                                    
                                            
                                    
                                    
                                    
                                        
                                    
                                    
            
           
    
    