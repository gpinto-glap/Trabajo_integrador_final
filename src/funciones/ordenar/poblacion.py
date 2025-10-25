import csv

def ordenar_poblacion():
    # Abrimos el CSV y leemos todas las filas
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = list(csv.DictReader(archivo))

    # Preguntamos al usuario cómo quiere ordenar
    print("Opciones de orden por población:")
    print("1 - De menor a mayor población")
    print("2 - De mayor a menor población")
    opcion = input("Elegí una opción (1/2): ").strip()

    if opcion == "1":
        # Orden ascendente por población
        ordenado = sorted(lector, key=lambda fila: int(fila['poblacion']))
    elif opcion == "2":
        # Orden descendente por población
        ordenado = sorted(lector, key=lambda fila: int(fila['poblacion']), reverse=True)
    else:
        print("Opción inválida")
        return

    # Imprimir todos los países ordenados
    for fila in ordenado:
        print(f"Nombre: {fila['nombre']}, Población: {fila['poblacion']}, Superficie: {fila['superficie']}, Continente: {fila['continente']}")