# Librerias
import datetime


# Constantes que se reuitilizan en el codigo
CARNET = "carnet"
NOMBRE = "nombre"
CARRERA = "carrera"
NOTA = "nota"

# Se almacenaran los estudiantes en un diccionario 
estudiantes = {
    
}

# Funcion para almacenar estudiantes en el diccionario
def ingresar_est(carnet, nombre, carrrera):
    # Condicion para evitar modificar informacion ya existente
    if not buscar(carnet):
        estudiantes[carnet] = {NOMBRE:nombre, CARRERA:carrrera, NOTA:0}
        resultado = f"Estudiante {carnet} {nombre} registrado exitosamente en {carrera}"
    else:
    # Mensaje de error
        resultado = f"Duplicado: Carnet {carnet} ya registrado"
    return resultado

# Funcion para buscar estudiantes
# Segun el carnet y retorna un valor booleano
def buscar(carnet):
    return carnet in estudiantes

# Funcion para actualizar la informacion de un estudiante
# Segun el carnet
# Solicita el dato a actualizar y el nuevo valor
def actualizar(carnet, dato, valor):
    estudiantes[carnet][dato] = valor
    return f"Estudiante {carnet} actualizado"

# Funcion para escribir los datos almacenados en formato csv
def exportar():
    # Crear o sobreescribir el archivo
    acta = open("acta.csv", "wt")
    # Agregar el campo fecha
    acta.write("fecha de acta\n")
    # Agregar el valor de la fecha de hoy
    # En formato d-m-y
    acta.write(f"{datetime.datetime.now().strftime('%d-%m-%y')}")
    # Agregar las siguientes columnas
    acta.write("\n\n")
    acta.write(f"{CARNET}, {NOMBRE}, {CARRERA}, {NOTA}")
    # Agregar los valores almacenados en el diccionario
    for est in estudiantes:
        acta.write(f"\n{est}, {estudiantes[est][NOMBRE]}, {estudiantes[est][CARRERA]}, {estudiantes[est][NOTA]}")
    # Agregar el promedio de las notas ingresadas
    acta.write("\n\npromedio\n")
    # Obtener las notas como un arreglo/lista
    acta.write(f"{promedio([estudiantes[x][NOTA] for x in estudiantes])}\n")
    # Cerrar el archivo
    acta.close()

# Funcion para obtener el promedio de las notas
def promedio(notas):
    promedio = 0
    for nota in notas:
        promedio += nota
    promedio /= len(notas)
    return promedio

# Funcion para imprimir el diccionario
def resumen():
    resultado = ""
    # Se recorre el diccionario y se concatenan los datos de cada estudiante
    # Cada estudiante se imprime en una sola linea
    for est in estudiantes:
        resultado += f"\n{est} {estudiantes[est][NOMBRE]} {estudiantes[est][CARRERA]} {estudiantes[est][NOTA]}"
    return resultado


# Menu
print("Bienvenido")
print("Ingrese el numero correspondiente a la opcion que desea ejecutar")
#salir = False
resultado = ""
while True:
    # Mostrar el menu con sus opciones
    print("1. Ingresar datos de estudiantes\n2. Ingresar notas de estuiante\n3. Exportar aca de notas\n4. Salir")
    match input("Que desea realizar? "):
        case "1":
            # Solicitud de datos para almacenar
            try:
                n = int(input("Cuantos estudiantes desea ingresar: "))
            except:
                print("Ingrese un valor entero")
            else:
                for x in range(n):
                    carnet = input("Ingrese el carnet del estudiante: ")
                    nombre = input("Ingrese el nombre del estudiante: ")
                    carrera = input("Ingrese la carrera del estudiante: ")
                    print()
                    # Condicion para evitar informacion vacia
                    if carnet and nombre and carrera:
                        # Se imprime el resultado
                        resultado += "\n"
                        resultado += ingresar_est(carnet, nombre, carrera)
                    else:
                        # Mensaje de error
                        resultado = "Por favor no dejar vacios los campos"
        case "2":
            # Se solicita el carnet a buscar
            carnet = input("Ingrese el carnet a actualizar: ")
            # Si el carnet se encuentra almacenado se muestran los datos asociados
            # Sino se despliega un mensaje al usuario
            if buscar(carnet):
                print(f"Estudiante {carnet} {estudiantes[carnet][NOMBRE]} en {estudiantes[carnet][CARRERA]} con nota {estudiantes[carnet][NOTA]}")

                # Se le pregunta al usuario si desea cambiar la nota
                # Cualquier otro valor que no sea el caracter 'S' o 's' se tomara como no
                if input("Desea cambiar la nota? [S][N] ") == "S":
                    while True:
                        try:
                            valor = float(input("Ingrese la nueva nota: "))
                        except:
                            print("Ingrese un numero")
                        else:
                            resultado = actualizar(carnet, NOTA, valor)
                            break
                else:
                    resultado = "No se cambiaron datos"
            else:
                resultado = "Estudiante no registrado"
        case "3":
            exportar()
            resultado = "Acta generada exitosamente"
        case "4":
            # Break para cerrrar el ciclo while
            print("Estudiantes que se trabajaron en esta sesión")
            print(resumen())
            break
        case _:
            resultado = "Ingrese el numero correspondiente a la opcion que desea"
    # Se imprime el resultado de la opcion solicitada
    print(resultado)
    # Pausa para que el usuario vea el resultado
    input()
print("Feliz dia")