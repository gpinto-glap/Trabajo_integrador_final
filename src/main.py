from funciones.getpaises.paises import get_paises
from funciones.buscar.nombre import buscar_pais
from funciones.filtrar.poblacion import buscar_poblacion
from funciones.menu.menu import menu_filtrar, menu_ordenar, menu_estadisticas

# LIBRERÍAS DE COLORES Y RECUSDRSOS (Rich)

from rich.console import Console
from rich.panel import Panel
from rich.style import Style # Opcional: Por si usamos estilos personalizados

# Se Inicializa la consola para usar las funciones de Rich
console = Console()


def main(): 
#docker run -it --rm -v ${PWD}:/app app:0.1
    bandera = True
    while bandera == True:
        print("""
        --------------------
        MENU DE OPCIONES
        --------------------
        1. BUSCAR POR NOMBRE DE PAIS
        2. FILTRAR
        3. ORDENAR
        4. ESTADISTICAS
        5. SALIR
            """) 
        opcion = input("Ingrese opción deseada: ")
        if opcion == "1":
            buscar_pais()
        elif opcion == "2":
            menu_filtrar()
        elif opcion == "3":
            menu_ordenar()
        elif opcion == "4":
            menu_estadisticas()
        elif opcion == "5":
            print("adios:)")
            bandera = False
        else:
            print("opcion invalida")

if __name__ == "__main__":
    # Llamada a la función principal
    main()
