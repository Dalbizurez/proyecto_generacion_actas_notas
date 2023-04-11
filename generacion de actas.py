

# Menu
print("Bienvenido")
print("Ingrese el numero correspondiente a la opcion que desea ejecutar")
#salir = False
while True:
    print("1. Ingresar datos de estudiantes\n2. Ingresar notas de estuiante\n3.Exportar aca de notas\n4. Salir")
    match input("Que desea realizar? "):
        case "1":
            pass
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
            print("Ingrese el numero correspondiente a la opcion que desea")