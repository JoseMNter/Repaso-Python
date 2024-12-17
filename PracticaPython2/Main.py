import RedSociales

redSocial = RedSociales.RedSocial()

def main():
    while True:
        opcion = int(input("Elige una opción:\n1) Crear un usuario\n2) Crear una publicación\n3) Agregar un comentario a una publicación\n4) Ver los detalles de una publicación\n5) Listar todos los usuarios\n6) Listar todas las publicaciones\n7) Ver los comentarios de una publicación\n8) Guardar datos en un archivo de texto\n9) Consultar datos\n10) Salir\n"))
        
        match opcion:
            case 1:
                # Crear un usuario
                id_usuario = int(input("Introduce la ID de usuario nuevo: "))
                
                # Verificar si ya existe un usuario con esa ID
                for usuario in redSocial.listaUsuarios:
                    if usuario.id == id_usuario:
                        print("Ya existe un usuario con esa ID.")
                        continue  # Saltar a la siguiente iteración si ya existe
                
                # Si no existe, creamos el usuario
                nombre = input("Escribe el nombre del nuevo usuario: ")
                email = input("Escribe el email del nuevo usuario: ")
                redSocial.registrar_usuario(id_usuario, nombre, email)
                print("Usuario creado.")
            
            case 2:
                # Crear una publicación
                publicacion_id = int(input("Introduce la ID de la nueva publicación: "))
                
                # Verificar si ya existe una publicación con esa ID
                for publicacion in redSocial.listaPublicaciones:
                    if publicacion.id_publicacion == publicacion_id:
                        print("Ya existe una publicación con esta ID.")
                        continue  # Saltar a la siguiente iteración si ya existe
                
                # Si no existe, creamos la publicación
                texto = input("Introduce el contenido de la publicación:\n")
                redSocial.crear_publicacion(publicacion_id, texto)
                print("Publicación creada.")
            
            case 3:
                # Agregar un comentario a una publicación
                idABuscar = int(input("Introduce la ID de la publicación para agregar un comentario: "))
                
                # Buscar y agregar el comentario a la publicación
                for publicacion in redSocial.listaPublicaciones:
                    if publicacion.id_publicacion == idABuscar:
                        comentario = input("Introduce tu comentario: ")
                        publicacion.agregarComentario(comentario)
                        print("Comentario agregado.")
                        break  # Salir del ciclo una vez encontrado
                else:
                    print("No se encontró la publicación.")
                    
            case 4:
                # Ver detalles de una publicación
                id_publicacion = int(input("Introduce la ID de la publicación para ver los detalles: "))
                
                # Buscar y mostrar detalles de la publicación
                for publicacion in redSocial.listaPublicaciones:
                    if publicacion.id_publicacion == id_publicacion:
                        publicacion.ver_detalles()
                        break
                else:
                    print("No se encontró la publicación.")
                        
            case 5:
                # Listar todos los usuarios
                print("Usuarios registrados:")
                for usuario in redSocial.listaUsuarios:
                    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Email: {usuario.email}")
            
            case 6:
                # Listar todas las publicaciones
                print("Publicaciones creadas:")
                for publicacion in redSocial.listaPublicaciones:
                    print(f"ID: {publicacion.id_publicacion}, Contenido: {publicacion.contenido}")
            
            case 7:
                # Ver comentarios de una publicación
                id_publicacion = int(input("Introduce la ID de la publicación para ver los comentarios: "))
                
                # Buscar y mostrar los comentarios de la publicación
                for publicacion in redSocial.listaPublicaciones:
                    if publicacion.id_publicacion == id_publicacion:
                        comentarios = publicacion.ver_comentarios()
                        print("Comentarios:")
                        for comentario in comentarios:
                            print(f"- {comentario}")
                        break
                else:
                    print("No se encontró la publicación.")
            
            case 8:
                
                with open('usuarios.txt', 'a') as file:  # 'a' para agregar contenido sin sobrescribir
                    for usuario in redSocial.listaUsuarios:
                        file.write(f"{usuario.id},{usuario.nombre},{usuario.email}\n")
                print("Usuarios guardados correctamente.")
            
            case 9:
                
                with open('usuarios.txt','r') as file:
                    print("\n---Lista de usuarios registrados---")
                    for linea in file:
                        id,nombre,email = linea.strip().split(",")
                        print(f"ID: {id}, Nombre: {nombre}, Email: {email}")
                print("\n"*5)
            
            case 10:
                print("Cerrando...")
                break         

main()    
    
            
            
            
            
            
        
            
            
            
            
            
            
            
        
        
           
           
    
        
            

                
            
           
           