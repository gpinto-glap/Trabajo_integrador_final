from funciones.filtrar.poblacion import buscar_poblacion
from funciones.filtrar.superficie import buscar_superficie
from funciones.filtrar.continente import buscar_continente
def menu_filtrar():
    bandera = True
    while bandera == True:
        print("""
        ---------------------------
          MENU DE OPCIONES FILTRAR
        ----------------------------
        1. FILTRAR POR CONTINENTE
        2. FILTRAR POR POBLACION
        3. FILTRAR POR SUPERFICIE
        4. SALIR

        """)
        opcion = input("ingrese opcion deseada ")

        if opcion == "1": 
            buscar_continente()
        elif opcion == "2":
            buscar_poblacion()
        elif opcion == "3":
            buscar_superficie()
        elif opcion == "4":
            print("adios:)")
            bandera = False
        else:
            print("opcion invalida")

from funciones.ordenar.nombre import ordenar_nombre
from funciones.ordenar.poblacion import ordenar_poblacion
from funciones.ordenar.superficie import ordenar_superficie



def menu_ordenar():
    bandera = True
    while bandera == True:
        print("""
        ---------------------------
          MENU DE OPCIONES ORDENAR
        ---------------------------
        1. ORDENAR POR NOMBRE
        2. ORDENAR POR POBLACION
        3. ORDENAR POR SUPERFICIE
        4. SALIR
        """)
        opcion = input("ingrese opcion deseada ")

        if opcion == "1": 
            ordenar_nombre()
        elif opcion == "2":
            ordenar_poblacion()
        elif opcion == "3":
            ordenar_superficie()
        elif opcion == "4":
            print("adios:)")
            bandera = False
        else:
            print("opcion invalida")

from funciones.estadisticas.menor_mayor import estadisticas_poblacion


def menu_estadisticas():
    bandera = True
    while bandera == True:
        print("""
        -------------------------------
          MENU DE OPCIONES ESTADISTICAS
        -------------------------------
        1. PAIS CON MAYOR O MENOR POBLACION
        2. PROMEDIO DE POBLACION 
        3. PROMEDIO DE SUPERFICIE
        4. CANTIDAD DE PAISES POR CONTINENTE
        5. SALIR
        """)
        opcion = input("ingrese opcion deseada ")

        if opcion == "1": 
            estadisticas_poblacion()
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            print("adios:)")
            bandera = False
        else:
            print("opcion invalida")

