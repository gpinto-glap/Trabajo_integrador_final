import csv

def promedio_superficie():
    # Abrimos el CSV y leemos todas las filas
    with open("Trabajo_integrador_final-main/data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = list(csv.DictReader(archivo))

    # Preguntamos si quiere filtrar por continente
    filtro = input("¿Querés calcular el promedio solo de un continente? (s/n): ").strip().lower()
    if filtro == 's':
        continente = input("Ingresá el continente: ").strip().lower()
        # Filtramos solo los países que coincidan con el continente
        datos = [fila for fila in lector if fila['continente'].lower() == continente]
        if not datos:
            print(f"No se encontraron países en el continente '{continente}'")
            return
    else:
        datos = lector  # usamos todos los países

    # Calculamos el promedio
    total_superficie = sum(int(fila['superficie']) for fila in datos)
    promedio = total_superficie / len(datos)

    # Mostramos el resultado
    if filtro == 's':
        print(f"\nEl promedio de superficie de los países en {continente.title()} es: {promedio:,.0f}")
    else:
        print(f"\nEl promedio de superficie de todos los países es: {promedio:,.0f}")