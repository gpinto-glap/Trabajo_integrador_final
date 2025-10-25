import csv

def ordenar_nombre():
    # Abrimos el CSV y leemos todas las filas
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = list(csv.DictReader(archivo))

    # Preguntamos al usuario cómo quiere ordenar
    print("Opciones de orden por nombre:")
    print("1 - De la A a la Z (ascendente)")
    print("2 - De la Z a la A (descendente)")
    opcion = input("Elegí una opción (1/2): ").strip()

    if opcion == "1":
        # Orden ascendente
        ordenado = sorted(lector, key=lambda fila: fila['nombre'])
    elif opcion == "2":
        # Orden descendente
        ordenado = sorted(lector, key=lambda fila: fila['nombre'], reverse=True)
    else:
        print("Opción inválida")
        return

    # Imprimir todos los países ordenados
    for fila in ordenado:
        print(f"Nombre: {fila['nombre']}, Población: {fila['poblacion']}, Superficie: {fila['superficie']}, Continente: {fila['continente']}")