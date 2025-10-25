import csv

def buscar_pais():
    
    buscar_nombre: str=str(input("ingrese nombre del pais (completo/parcial) "))
    # Abrimos el CSV
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)  # convierte cada fila en un diccionario

        #buscamos coincidencia completa
        for fila in lector:
            if fila['nombre'].lower() == buscar_nombre.lower():  
                # Si coincide, imprimimos todos los datos
                print(f"Nombre: {fila['nombre']}")
                print(f"Población: {fila['poblacion']}")
                print(f"Superficie: {fila['superficie']}")
                print(f"Continente: {fila['continente']}")
                return  
            #buscamos coincidencia parcial (primeras 3 letras)
            elif fila['nombre'][:3].lower() == buscar_nombre[:3].lower(): 
                # Si coincide, imprimimos todos los datos
                print(f"Nombre: {fila['nombre']}")
                print(f"Población: {fila['poblacion']}")
                print(f"Superficie: {fila['superficie']}")
                print(f"Continente: {fila['continente']}")
                return

        
        print(f"No se encontró el país '{buscar_nombre}'")

