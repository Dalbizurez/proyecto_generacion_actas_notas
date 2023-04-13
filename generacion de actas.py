# Constantes que se reuitilizan en el codigo
NOMBRE = "nombre"
CARRERA = "carrera"
NOTA = "nota"

# Se almacenaran los estudiantes en un diccionario 
estudiantes = {
    
}

# Funcion para almacenar estudiantes en el diccionario
def ingresar_est(carnet, nombre, carrrera):
    # Condicion para evitar modificar informacion ya existente
    if not carnet in estudiantes:
        estudiantes[carnet] = {NOMBRE:nombre, CARRERA:carrrera, NOTA:0}
        resultado = f"Estudiante {carnet} {nombre} registrado exitosamente en {carrera}"
    else:
    # Mensaje de error
        resultado = f"Duplicado: Carnet {carnet} ya registrado"
    return resultado



# Menu
print("Bienvenido")
print("Ingrese el numero correspondiente a la opcion que desea ejecutar")
#salir = False
while True:
    # Mostrar el menu con sus opciones
    print("1. Ingresar datos de estudiantes\n2. Ingresar notas de estuiante\n3. Exportar aca de notas\n4. Salir")
    match input("Que desea realizar? "):
        case "1":
            # Opcion, solicitud de datos para almacenar
            carnet = input("Ingrese el carnet del estudiante: ")
            nombre = input("Ingrese el nombre del estudiante: ")
            carrera = input("Ingrese la carrera del estudiante: ")
            # Condicion para evitar informacion vacia
            if carnet and nombre and carrera:
                # Se imprime el resultado
                resultado = ingresar_est(carnet, nombre, carrera)
            else:
                # Mensaje de error
                resultado = "Por favor no dejar vacios los campos"
            
        case "2": 
            pass
        case "3":
            pass
        case "4":
            # Salir = True para romper el ciclo
            #salir = True
            # O podria ser solo un break
            break
        case _:
            resultado = "Ingrese el numero correspondiente a la opcion que desea"
    # Se imprime el resultado de la opcion solicitada
    print(resultado)
    # Pausa para que el usuario vea el resultado
    input()