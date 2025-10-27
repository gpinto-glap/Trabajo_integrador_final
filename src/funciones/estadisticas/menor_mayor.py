import csv

def estadisticas_poblacion():
    # Abrimos el CSV y leemos todas las filas
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = list(csv.DictReader(archivo))

    # Preguntamos si quiere filtrar por continente
    filtro = input("¿Querés filtrar por continente? (s/n): ").strip().lower()
    if filtro == 's':
        continente = input("Ingresá el continente: ").strip().lower()
        # Filtramos solo los países que coincidan con el continente
        datos = [fila for fila in lector if fila['continente'].lower() == continente]
        if not datos:
            print(f"No se encontraron países en el continente '{continente}'")
            return
    else:
        datos = lector  # usamos todos los países

    # Preguntamos la opción de estadística
    print("Opciones de estadística por población:")
    print("1 - Primeros 5 países de menor población")
    print("2 - Primeros 5 países de mayor población")
    opcion = input("Elegí una opción (1/2): ").strip()

    if opcion == "1":
        # Orden ascendente por población y tomamos los 5 primeros
        resultados = sorted(datos, key=lambda fila: int(fila['poblacion']))[:5]
    elif opcion == "2":
        # Orden descendente por población y tomamos los 5 primeros
        resultados = sorted(datos, key=lambda fila: int(fila['poblacion']), reverse=True)[:5]
    else:
        print("Opción inválida")
        return

    # Imprimir resultados
    print("\nResultados:")
    for fila in resultados:
        print(f"Nombre: {fila['nombre']}, Población: {fila['poblacion']}, Superficie: {fila['superficie']}, Continente: {fila['continente']}")