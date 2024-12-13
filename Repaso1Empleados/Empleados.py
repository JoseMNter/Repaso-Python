import json
empleados_dict = {
    101: {'id': 101, 'nombre': 'Juan', 'edad': 30, 'departamento': 'Ventas', 'salario': 3000},
    102: {'id': 102, 'nombre': 'Ana', 'edad': 25, 'departamento': 'Marketing', 'salario': 2800}
}

def agregarEmpleado():
        
        print("Vamos a agregar un empleado.")
        id = int(input("Introduce una ID única: "))
        
        if id in empleados_dict:
            print("Ya existe un empleado con esa ID")
        else:
            nombre = input("Introduce el nombre: ")
            edad = input("Introduce la edad: ")
            departamento = input("Introduce el departamento: ")
            salario = input("Introduce el salario: ")
            
            empleados_dict[id] = {
                "id": id,
                "nombre": nombre,
                "edad": edad,
                "departamento": departamento,
                "salario": salario
            }
            
            print(f"Empleado con la ID: {id} agregado correctamente.")
    
def buscarEmpleadoPorID():
        
        print("Vamos a buscar un empleado en la base de datos")
        idAbuscar=int(input("Introduce la ID: "))
        
        if idAbuscar in empleados_dict:
            empleado = empleados_dict[idAbuscar]
            print(f"La ID pertenece al empleado: {empleado['nombre']}")
            return empleado
        else:
            print(f"No se ha encontrado el empleado con la ID: {idAbuscar}")
            return None

def eliminarEmpleado():
    
    empleado_Eliminar=buscarEmpleadoPorID()
    
    if empleado_Eliminar:
        print("Eliminando al empleado de la base de datos..")
        del empleados_dict[empleado_Eliminar["id"]]
        print("Eliminado.")
        
def mostrarEmpleados():
    for empleado in empleados_dict.items():
        print(empleado)
           
        
def menuNteractivo(empleados_dict):
        
    print("Bienvenido a Nter, por favor, eliga una de estas opciones: ")
    while True:
        opcion=int(input("1) Agregar empleado\n2) Buscar empleado por ID\n3) Eliminar empleado por ID\n4) Mostrar todos los empleados\n5) Guardar empleados en un archivo\n6) Cargar empleados desde un archivo\n7) Salir\n"))
        
        if opcion not in [1,2,3,4,5,6,7]:
            print("Error, introduce el número correcto para acceder a la opción")
            continue
                
    
        match opcion:
            case 1:
                agregarEmpleado()
            case 2:
                buscarEmpleadoPorID()
            case 3:
                eliminarEmpleado()
            case 4:
                mostrarEmpleados()
            case 5:
                with open("empleados.json","w") as file:
                    json.dump(empleados_dict,file,indent=4)
                    print("Se ha guardado correctamente en el archivo.")
            case 6:
                with open("empleados.json","r") as file:
                    empleados_dict=json.load(file)
                    print("Empleados cargados correctamente.")
            case 7:
                print("Cerrando la aplicación...")
                break

menuNteractivo(empleados_dict)
                
                
                
                
                
                    
                    
                