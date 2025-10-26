import csv
from rich.console import Console
from rich.table import Table
from rich.style import Style
import os # Necesario para limpiar la consola

def buscar_continente():
  
    
    console = Console()
    continente_busqueda = input("Ingresá el continente: ").strip().lower()
  
    try:   # 2. Lectura y Filtrado del CSV
        with open("data/paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            resultados = [
                fila for fila in lector
                if fila.get('continente', '').lower() == continente_busqueda
            ]
    except FileNotFoundError:
        console.print("[bold red]¡Error![/bold red] Archivo 'data/paises.csv' no encontrado.")
        return
    
    if not resultados:
        console.clear()
        console.print(f"[bold red]No se encontraron países[/bold red] en el continente '[cyan]{continente_busqueda.capitalize()}[/cyan]'", style="white")
        input("\nPresiona [Enter] para continuar...")
        return

    
    items_por_pagina = 10 #Paginación
    total_paginas = (len(resultados) + items_por_pagina - 1) // items_por_pagina

    for num_pagina in range(total_paginas):
        console.clear()

        #Crear la tabla 
        tabla = Table(title=f"Países en [bold yellow]{continente_busqueda.capitalize()}[/bold yellow] (Pág. {num_pagina + 1}/{total_paginas})", 
                      show_header=True, header_style="bold green")

        # Estilos para los datos
        estilos_datos = [Style(color="cyan"), Style(color="magenta"), Style(color="yellow"), Style(color="green")]
        
        # Columnas con estilo bold
        encabezados = ['Nombre', 'Poblacion', 'Superficie', 'Continente']
        for i, encabezado in enumerate(encabezados):
            # Usamos el color de estilo_datos para el texto, pero mantenemos el bold green para el encabezado
            tabla.add_column(encabezado.capitalize(), style=estilos_datos[i % len(estilos_datos)], justify="left")

        # Determinar el rango de resultados para la página actual
        inicio = num_pagina * items_por_pagina
        fin = min((num_pagina + 1) * items_por_pagina, len(resultados))
        
        # Añadir las filas a la tabla
        for fila in resultados[inicio:fin]:
            tabla.add_row(
                fila['nombre'],
                fila['poblacion'],
                fila['superficie'],
                fila['continente']
            )

        # Imprimir la tabla
        console.print(tabla)
        
        # Esperar la entrada para la siguiente página
        if num_pagina < total_paginas - 1:
            console.print("\n[bold blue]Presiona ENTER para ver la siguiente página...[/bold blue]", end="") #Imprime el mensaje con colores ya que input no puede ir en colores
            input()  # se usa input() sin texto para pausar y esperar la entrada

        else:
            console.print("\n[bold blue]Fin de la lista.[/bold blue]")

# Llamada a la función para probar
# buscar_continente()