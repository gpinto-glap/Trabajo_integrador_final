import csv

def paises_por_continente():
    # Abrimos el archivo CSV
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = list(csv.DictReader(archivo))

    # Pedimos el continente (obligatorio)
    continente = input("Ingresá el nombre del continente: ").strip().lower()

    # Filtramos los países que pertenezcan a ese continente
    datos = [fila for fila in lector if fila['continente'].lower() == continente]

    # Si no se encontraron países, avisamos
    if not datos:
        print(f"No se encontraron países en el continente '{continente}'.")
        return

    # Contamos la cantidad de países
    cantidad = len(datos)

    # Mostramos el resultado
    print(f"\nLa cantidad de países en {continente.title()} es: {cantidad}")