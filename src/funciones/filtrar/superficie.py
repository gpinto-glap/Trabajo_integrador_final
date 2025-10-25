import csv

def buscar_superficie():
    # Abrimos el CSV
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = list(csv.DictReader(archivo))  # guardamos todas las filas en una lista

    # Menú de opciones
    print("Opciones de búsqueda por superficie:")
    print("1 - Paises con superficie mayor a un número")
    print("2 - Paises con superficie menor a un número")
    print("3 - Paises con superficie entre dos números")
    opcion = input("Elegí una opción (1/2/3): ")

    if opcion == "1":
        numero = int(input("Ingresá el número mínimo de superficie: "))
        resultados = [fila for fila in lector if int(fila['superficie']) > numero]

    elif opcion == "2":
        numero = int(input("Ingresá el número máximo de superficie: "))
        resultados = [fila for fila in lector if int(fila['superficie']) < numero]

    elif opcion == "3":
        min_num = int(input("Ingresá el número mínimo de superficie: "))
        max_num = int(input("Ingresá el número máximo de superficie: "))
        resultados = [fila for fila in lector if min_num <= int(fila['superficie']) <= max_num]

    else:
        print("Opción inválida")
        return

    # Mostrar resultados
    if resultados:
        for fila in resultados:
            print(f"Nombre: {fila['nombre']}, Población: {fila['poblacion']}, Superficie: {fila['superficie']}, Continente: {fila['continente']}")
    else:
        print("No se encontraron países que cumplan la condición")