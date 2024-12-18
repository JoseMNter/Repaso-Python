import json

listaEmpleados = [
    {
        'ID': 1,
        'Nombre': 'Juan Pérez',
        'Edad': 30,
        'Departamento': 'Ventas',
        'Salario': 2500.0
    }
]

def main(listaEmpleados):
    
    while True:
        
        opcion = int(input("Elige una de las siguientes opciones:\n1) Agregar empleado\n2) Buscar empleado por ID\n3) Eliminar empleado por ID\n4) Mostrar todos los empleados\n5) Guardar empleados en un archivo\n6) Cargar empleados desde un archivo\n7) Salir\n"))
        
        match opcion:
            
            case 1:
                
               id_empleado = int(input("Introduce una ID única: "))
               
               for empleado in listaEmpleados:
                   if empleado['ID'] == id_empleado:
                       print("Ya existe esa ID.")
                       break
                   else:
                       nombre = input("Introduce el nombre del empleado: ")
                       
                       try:
                           
                        edad= int(input("Introduce la edad del empleado: "))
                        
                       except ValueError:
                           print("Error: Ingresa un valor válido.\n")
                           break
        
                       departamento = input("Introduce su departamento: ")
                       salario = float(input("Introduce su salario: "))
                       listaEmpleados.append({
                           'ID':id_empleado,
                           'Nombre':nombre,
                           'Edad':edad,
                           'Departamento':departamento,
                           'Salario':salario
                       })
                       print("Empleado agregado correctamente.\n")
                
            case 2:
                
                idABuscar = int(input("Introduce la ID a buscar: "))
                
                for empleado in listaEmpleados:
                    
                    if empleado['ID'] == idABuscar:
                        empleado_encontrado=empleado
                        print(empleado_encontrado)
                    else:
                        print('No se ha encontrado el empleado.')
                        
            
            case 3:
                
                idABuscar = int(input("Introduce la ID del empleado para eliminar: "))
            
                for empleado in listaEmpleados:
                    
                    if listaEmpleados['ID'] == idABuscar:
                        
                        listaEmpleados.remove(empleado)
                        print("Empleado eliminado correctamente.\n")
                        break
                        
                    else:
                        print('No se ha encontrado el empleado.')
            
            case 4:
                
                print("---- Lista de empleados ----")
                
                for empleado in listaEmpleados:
                    
                    print(f"{empleado}\n")
                    
            case 5:
                
                print("Guardando empleados en un archivo de texto...\n")
                
                with open('empleados.json','w') as archivo:
                    
                    json.dump(listaEmpleados,archivo, indent=4)
                    
                print("Guardado.\n")
                
            case 6:
                
                try:
                    with open('empleados.json','r') as archivo:
                        listaEmpleados.clear()
                        listaEmpleados.extend(json.load(archivo))
                    print("Empleados cargados correctamente desde el archivo.\n")
                except FileNotFoundError:
                    print("No se encontró el archivo. Lista vacía")
                    
            case 7:
                print("Saliendo..")
                break
            
            case _:
                print("Opción no válida.\n")
                
main(listaEmpleados)
                        
                        
                       
        
        
    
    