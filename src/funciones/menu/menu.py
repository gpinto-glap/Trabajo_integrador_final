from funciones.filtrar.poblacion import buscar_poblacion
from funciones.filtrar.superficie import buscar_superficie
from funciones.filtrar.continente import buscar_continente
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

def menu_filtrar():
    bandera = True
    while bandera == True:
        console.clear() # Limpia la pantalla al inicio
        
        menu_text = Text() 
        
        # Título del menú
        menu_text.append("---------------------------------\n", style="bold white")
        menu_text.append("🌎 MENÚ DE OPCIONES: FILTRAR 🔎\n", style="bold #0099ff on black")
        menu_text.append("---------------------------------\n\n", style="bold white")
        
        # Opciones con Emojis y Colores
        menu_text.append("1. 🗺️  FILTRAR POR CONTINENTE\n", style="bold green")
        menu_text.append("2. 👨‍👩‍👧‍👦 FILTRAR POR POBLACIÓN\n", style="bold yellow")
        menu_text.append("3. 📐  FILTRAR POR SUPERFICIE\n", style="bold magenta")
        menu_text.append("4. 🔙  VOLVER AL MENÚ ANTERIOR\n", style="bold red")

        console.print(Panel(menu_text, title="Opciones de Filtrado", border_style="cyan"))
        opcion = input("Ingrese opción deseada: ").strip()

        if opcion == "1": 
            console.clear()
            buscar_continente()
        elif opcion == "2":
            console.clear()
            buscar_poblacion()
        elif opcion == "3":
            console.clear()
            buscar_superficie()
        elif opcion == "4":
            console.clear()
            console.print("[bold blue ]Volviendo al menú principal...[/bold blue]")
            bandera = False
        else:
            console.print("[bold yellow]:warning: OPCIÓN INVÁLIDA :warning:[/bold yellow]")
            input("Presiona [Enter] para continuar...")

from funciones.ordenar.nombre import ordenar_nombre
from funciones.ordenar.poblacion import ordenar_poblacion
from funciones.ordenar.superficie import ordenar_superficie



def menu_ordenar():
    bandera = True
    while bandera == True:
       console.clear() 
        
       menu_text = Text()
        
        # Título del menú
       menu_text.append("---------------------------------\n", style="bold white")
       menu_text.append("🌎 MENÚ DE OPCIONES: ORDENAR ↕️\n", style="bold #ff6600 on black")
       menu_text.append("---------------------------------\n\n", style="bold white")
        
        # Opciones con Emojis y Colores
       menu_text.append("1. 🅰️  ORDENAR POR NOMBRE\n", style="bold green")
       menu_text.append("2. 📈  ORDENAR POR POBLACIÓN\n", style="bold yellow")
       menu_text.append("3. ⛰️  ORDENAR POR SUPERFICIE\n", style="bold magenta")
       menu_text.append("4. 🔙  VOLVER AL MENÚ ANTERIOR\n", style="bold red")
        
        # Imprimimos el menú en un Panel
       console.print(Panel(menu_text, title="Opciones de Ordenamiento", border_style="orange3"))
        
       opcion = input("Ingrese opción deseada: ").strip()

       if opcion == "1": 
            console.clear()
            ordenar_nombre()
       elif opcion == "2":
            console.clear()
            ordenar_poblacion()
       elif opcion == "3":
            console.clear()
            ordenar_superficie()
       elif opcion == "4":
            console.clear()
            console.print("[bold blue ]Volviendo al menú principal...[/bold blue]")
            bandera = False
       else:
            console.print("[bold yellow]:warning: OPCIÓN INVÁLIDA :warning:[/bold yellow]")
            input("Presiona [Enter] para continuar...")

from funciones.estadisticas.menor_mayor import estadisticas_poblacion
from funciones.estadisticas.promedio_poblacion import promedio_poblacion
from funciones.estadisticas.promedio_superficie import promedio_superficie
from funciones.estadisticas.paises_continente import paises_por_continente


def menu_estadisticas():
    bandera = True
    while bandera == True:
        #console.clear()
        menu_text = Text()
        
        # Título del menú
        menu_text.append("------------------------------------\n", style="bold white")
        menu_text.append("🌎 MENÚ DE OPCIONES: ESTADÍSTICAS 📊\n", style="bold #aa00ff on black")
        menu_text.append("------------------------------------\n\n", style="bold white")
        
        # Opciones con Emojis y Colores
        menu_text.append("1. 🔝  PAÍS CON MAYOR O MENOR POBLACIÓN\n", style="bold green")
        menu_text.append("2. ⚖️  PROMEDIO DE POBLACIÓN\n", style="bold yellow")
        menu_text.append("3. 📏  PROMEDIO DE SUPERFICIE\n", style="bold magenta")
        menu_text.append("4. 🧩  CANTIDAD DE PAÍSES POR CONTINENTE\n", style="bold cyan")
        menu_text.append("5. 🔙  VOLVER AL MENÚ ANTERIOR\n", style="bold red")

        # Imprimimos el menú en un Panel 
        console.print(Panel(menu_text, title="Opciones Estadísticas", border_style="purple"))
        opcion = input("Ingrese opción deseada: ").strip()

        if opcion == "1": 
            console.clear()
            estadisticas_poblacion()
        elif opcion == "2":
            console.clear()
            promedio_poblacion()
        elif opcion == "3":
            console.clear()
            promedio_superficie()
        elif opcion == "4":
            console.clear()
            paises_por_continente()
        elif opcion == "5":
            console.clear()
            console.print("[bold blue ]Volviendo al menú principal...[/bold blue]")
            bandera = False
        else:
            console.print("[bold yellow]:warning: OPCIÓN INVÁLIDA :warning:[/bold yellow]")
            input("Presiona [Enter] para continuar...")