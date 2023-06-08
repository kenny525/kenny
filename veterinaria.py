import random
import msvcrt as ms

# Lista para almacenar los registros de mascotas
mascotas = []

def grabarmascota():
    print("=== Grabar/Registrar Mascota ===")
    
    
    
    

    # Validar ID Mascota
    while True:
        idmascota=input("ID Mascota: ")
        if len(idmascota) != 5 or not idmascota.isdigit():
            print("Error: ID Mascota debe ser numérico y tener 5 dígitos.")
        else:
            break
            

    # Validar Nombre Mascota
    while True:
        nommascota=input("Nombre Mascota: ")
        if nommascota == "":
            print("Error: Nombre Mascota no puede estar vacío.")
        else:
            break
            

    # Validar Nombre Dueño
    while True:
        nomdueno=input("Nombre Dueño: ")
        if nomdueno == "":
            print("Error: Nombre Dueño no puede estar vacío.")
        else:
            break
        

    # Validar Tipo
    while True:
            tipo=input("Tipo (Perro o Gato): ")
            if tipo != "Perro" and tipo != "Gato":
                print("Error: Tipo debe ser Perro perro o Gato gato.")
            else:
                break
        

    # Agregar registro a la lista de mascotas
    mascota = {
        "ID Mascota": idmascota,
        "Nombre Mascota": nommascota,
        "Nombre Dueño": nomdueno,
        "Tipo": tipo
    }
    mascotas.append(mascota)
    print("Mascota registrada exitosamente")
    

def listarregistros():
        print("Listar Todos los registros")
        if len(mascotas) == 0:
            print("No hay registros de mascotas.")
        else:
            for mascota in mascotas:
                print("ID Mascota:", mascota["ID Mascota"])
                print("Nombre:", mascota["Nombre Mascota"])
                print("Tipo:", mascota["Tipo"])
                print("Dueño de la Mascota:")
                print("Sr/a:", mascota["Nombre Dueño"])
                print()
        print("Presione una tecla para continuar.")
        ms.getch()
        
    



def buscarmascota():
    
        print("=== Buscar Mascota ===")
        idmascota = input("Ingrese el ID Mascota: ")
        encontrado = False
        for mascota in mascotas:
            if mascota["ID Mascota"] == idmascota:
                print("ID Mascota:", mascota["ID Mascota"])
                print("Nombre:", mascota["Nombre Mascota"])
                print("Tipo:", mascota["Tipo"])
                print("Dueño de la Mascota:")
                print("Sr/a:", mascota["Nombre Dueño"])
                encontrado = True
                break
        if not encontrado:
            print("No se encontró la mascota con el ID proporcionado.")
        

def imprimirxreportes():
    
        print("Imprimir Reportes por tipo de mascota")
        tipo_mascota = input("ELIGA EL REPORTE\n1 - Perros\n2 - Gatos: ")
        if tipo_mascota == "1":
            tipo = "Perro"
        elif tipo_mascota == "2":
            tipo = "Gato"
        else:
            print("Opción inválida.")
            

        print("REPORTES")
        for mascota1 in mascotas:
            if mascota1["Tipo"] == tipo:
                print("ID Mascota:", mascota1["ID Mascota"])
                print("Nombre:", mascota1["Nombre Mascota"])
                print()
                print("Tipo:", mascota1["Tipo"])
                print("Dueño de la Mascota:")
                print("Sr/a:", mascota1["Nombre Dueño"])
                print("A su mascota le faltan", random.randint(1, 10), "vacunas")
                print()

# Menú principal
while True:
    print("===============================")
    print("=== SISTEMA DE REGISTRO ===")
    print("1. Grabar/Registrar Mascota")
    print("2. Listar Todos los registros")
    print("3. Buscar Mascota")
    print("4. Imprimir Reportes por tipo mascota")
    print("0. Salir")
    opcion = input("Ingrese una opción: ")
    
    if opcion == "1":
        grabarmascota()
    elif opcion == "2":
        listarregistros()
    elif opcion == "3":
        buscarmascota()
    elif opcion == "4":
        imprimirxreportes()
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Intente nuevamente.")