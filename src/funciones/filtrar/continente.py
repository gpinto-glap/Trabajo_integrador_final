import csv

def buscar_continente():
    continente_busqueda = input("Ingresá el continente: ").strip().lower()  # sacamos espacios y pasamos a minúsculas

    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        resultados = []
        for fila in lector:
            if fila['continente'].lower() == continente_busqueda:
                resultados.append(fila)

        if resultados:
            for fila in resultados:
                print(f"Nombre: {fila['nombre']}, Población: {fila['poblacion']}, Superficie: {fila['superficie']}, Continente: {fila['continente']}")
        else:
            print(f"No se encontraron países en el continente '{continente_busqueda}'")