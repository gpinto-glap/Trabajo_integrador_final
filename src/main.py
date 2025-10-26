from funciones.getpaises.paises import get_paises
from funciones.buscar.nombre import buscar_pais
from funciones.filtrar.poblacion import buscar_poblacion
from funciones.menu.menu import menu_filtrar, menu_ordenar, menu_estadisticas

# LIBRERÍAS DE COLORES Y RECUSDRSOS (Rich)

from rich.console import Console
from rich.panel import Panel
from rich.style import Style # Opcional: Por si usamos estilos personalizados
from rich.text import Text

# Se Inicializa la consola para usar las funciones de Rich
console = Console()


def main(): 
#docker run -it --rm -v ${PWD}:/app app:0.1
    bandera = True
    while bandera == True:
        console.clear()
       
        menu_text = Text() # 2. Definición del texto del menú con Emojis y Colores
        
        # Título del menú en color y negrita
        menu_text.append("--------------------\n", style="bold white")
        menu_text.append("🌎 MENÚ PRINCIPAL 🌍\n", style="bold #00ffaa on black")
        menu_text.append("--------------------\n\n", style="bold white")
        
        # Opciones con diferentes colores y emoticones
        menu_text.append("1. 🔎 BUSCAR POR NOMBRE DE PAÍS\n", style="bold green")
        menu_text.append("2. 🧩 FILTRAR PAÍSES\n", style="bold yellow")
        menu_text.append("3. 📝 ORDENAR PAÍSES\n", style="bold magenta")
        menu_text.append("4. 📊 ESTADÍSTICAS\n", style="bold cyan")
        menu_text.append("5. 👋 SALIR\n", style="bold red")

        # 3. Imprimimos el menú usando rich (opcionalmente con un Panel)
        console.print(Panel(menu_text, title="Opciones", border_style="blue"))
        opcion = input("Ingrese opción deseada: ")
        if opcion == "1":
            console.clear()
            buscar_pais()
        elif opcion == "2":
            console.clear()
            menu_filtrar()
        elif opcion == "3":
            console.clear()
            menu_ordenar()
        elif opcion == "4":
            console.clear()
            menu_estadisticas()
        elif opcion == "5":
            console.clear()
            console.print("[bold blue ]Gracias por usar nuestra aplicación:)[/bold blue]")
            bandera = False
        else:
            console.print("[yellow]:warning-text:[/yellow] [bold red] OPCION INVALIDA [/bold red] [yellow]:warning-text:[/yellow]")
            console.print ("[yellow] Intente de nuevo[/yellow]" )

if __name__ == "__main__":
    # Llamada a la función principal
    main()
