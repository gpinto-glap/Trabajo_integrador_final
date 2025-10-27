import csv
from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich import print # Importamos print de Rich para el menú y errores

def buscar_poblacion():
    console=Console()
    # Abrimos el CSV
    try:
        with open("Trabajo_integrador_final-main/data/paises.csv", "r", encoding="utf-8") as archivo:
            # Guardamos todas las filas en una lista para poder filtrarlas y paginarlas
            lector = list(csv.DictReader(archivo)) 
    except FileNotFoundError:
        console.print("[bold red]¡Error![/bold red] Archivo 'data/paises.csv' no encontrado.")
        return
    console.clear()
        
    # Menú de opciones
    console.print("[bold white]Opciones de búsqueda por población:[/bold white]")
    console.print("1 - Paises con población [bold green]MAYOR[/bold green] a un número")
    console.print("2 - Paises con población [bold red]MENOR[/bold red] a un número")
    console.print("3 - Paises con población [bold yellow]entre[/bold yellow] dos números")
    opcion = input("Elegí una opción (1/2/3): ")
    resultados= []

    if opcion == "1":
        try:
            numero = int(input("Ingresá el número mínimo de población: "))
            resultados = [fila for fila in lector if int(fila.get('poblacion', 0)) > numero]
            titulo_tabla = f"Países con Población > [cyan]{numero:,}[/cyan]"
        except ValueError:
            console.print("[bold red]¡ERROR![/bold red] [yellow]Debes ingresar un número válido.[/yellow]")
            return
        
        
    elif opcion == "2":
        try:
            numero = int(input("Ingresá el número máximo de población: "))
            resultados = [fila for fila in lector if int(fila.get('poblacion', 0)) < numero]
            titulo_tabla = f"Países con Población < [cyan]{numero:,}[/cyan]"
        except ValueError:
            console.print("[bold red]¡ERROR![/bold red] [yellow]Debes ingresar un número válido.[/yellow]")
            return
        

    elif opcion == "3":
        try:
            min_num = int(input("Ingresá el número mínimo de población: "))
            max_num = int(input("Ingresá el número máximo de población: "))
            resultados = [fila for fila in lector if min_num <= int(fila.get('poblacion', 0)) <= max_num]
            titulo_tabla = f"Países con Población entre [cyan]{min_num:,}[/cyan] y [cyan]{max_num:,}[/cyan]"
        except ValueError:
            console.print("[bold red]¡ERROR![/bold red] [yellow]Debes ingresar números válidos.[/yellow]")
            return
       
    else:
        console.print("[yellow]Opción inválida[/yellow]")
        return
# Paginación
    if not resultados:
        console.print("\n[bold yellow]No se encontraron países que cumplan la condición.[/bold yellow]")
        return

    ITEMS_POR_PAGINA = 15
    total_paginas = (len(resultados) + ITEMS_POR_PAGINA - 1) // ITEMS_POR_PAGINA

    estilos_datos = [Style(color="cyan"), Style(color="magenta"), Style(color="yellow"), Style(color="green")]
    encabezados = ['Nombre', 'Poblacion', 'Superficie', 'Continente']
    for num_pagina in range(total_paginas):
        console.clear() 

        # Crear la tabla 
        tabla = Table(title=f"{titulo_tabla} (Pág. {num_pagina + 1}/{total_paginas})", 
                      show_header=True, header_style="bold green")

        
        for i, encabezado in enumerate(encabezados): # Añadir las columnas con estilo bold
            tabla.add_column(encabezado.capitalize(), style=estilos_datos[i % len(estilos_datos)], justify="left") # Aplica un color de estilo_datos diferente a cada columna
            inicio = num_pagina * ITEMS_POR_PAGINA # Determinar el rango de resultados para la página actual
            fin = min((num_pagina + 1) * ITEMS_POR_PAGINA, len(resultados))
        
        for fila in resultados[inicio:fin]: # Añadir las filas a la tabla
            # Usar los separadores de miles para mejor lectura
            tabla.add_row(
                fila['nombre'],
                f"{int(fila.get('poblacion', 0)):,}", 
                f"{int(fila.get('superficie', 0)):,}", 
                fila['continente']
            )

        # Imprimir la tabla
        console.print(tabla)
        
        # Pausar y esperar la entrada para la siguiente página 
        if num_pagina < total_paginas - 1:
            console.print("\n[bold blue]Presiona ENTER para ver la siguiente página...[/bold blue]", end="")
            input()
        else:
            console.print("\n[bold blue]Fin de la lista. Presiona ENTER para continuar.[/bold blue]", end="")
            input()
    