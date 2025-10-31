import csv
import sys
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.style import Style

# Inicializa la consola de Rich
console = Console()

# --- FUNCIONES AUXILIARES  ---

def formato_numero_rich(numero: str, style_color: str) -> str:
    """Formatea un número con separadores de miles y color usando Rich."""
    try:
        num = int(numero)
        return f"[{style_color}]{num:,.0f}[/]".replace(",", ".") 
    except (ValueError, TypeError):
        return f"[bold red]{numero}[/bold red]" 

def obtener_valor_seguro(fila, clave):
    """Obtiene el valor de la clave, manejando posibles ausencias o errores."""
    return fila.get(clave, "N/A")

def imprimir_tabla_paginada_rich(data, continente, total_paises, elementos_por_pagina=10):
    """Imprime la lista de países paginada con diseño Rich."""
    
    total_elementos = len(data)
    total_paginas = (total_elementos + elementos_por_pagina - 1) // elementos_por_pagina
    
    # Definición de estilos para las columnas (solo las necesarias)
    estilos_datos = [
        Style(color="cyan"),      # Nombre
        Style(color="yellow"),    # Población
        Style(color="green")      # Superficie
    ]
    encabezados = ['Nombre', 'Población', 'Superficie']
    
    for pagina_indice in range(0, total_elementos, elementos_por_pagina):
        pagina_actual = (pagina_indice // elementos_por_pagina) + 1
        elementos_pagina = data[pagina_indice:pagina_indice + elementos_por_pagina]
        
        # 1. Crear la Tabla
        titulo_tabla = f"Países de {continente.title()} ({total_paises} en total)"
        table = Table(
            title=titulo_tabla, 
            show_header=True, 
            header_style="bold white on #4078c0",
            border_style="dim yellow",
            title_style="bold yellow underline"
        )

        # 2. Definir Columnas
        for i, encabezado in enumerate(encabezados):
            table.add_column(
                encabezado, 
                style=estilos_datos[i % len(estilos_datos)], 
                justify="right" if encabezado != 'Nombre' else "left"
            )

        # 3. Agregar Filas
        for fila in elementos_pagina:
            poblacion = formato_numero_rich(obtener_valor_seguro(fila, 'poblacion'), 'yellow')
            superficie = formato_numero_rich(obtener_valor_seguro(fila, 'superficie'), 'green')
            nombre_pais = Text(obtener_valor_seguro(fila, 'nombre'), style="bold cyan")

            table.add_row(
                nombre_pais, 
                poblacion,
                superficie
            )

        # 4. Imprimir la información de la página y la tabla
        console.clear()
        
        # Panel para la paginación
        console.print(Panel(
            f"Página [bold magenta]{pagina_actual}[/bold magenta] de [bold magenta]{total_paginas}[/bold magenta]", 
            title="🌍 Conteo por Continente",
            title_align="left",
            border_style="magenta"
        ))
        
        console.print(table)
        
        # 5. Pausa si no es la última página (Con opción de Salir 'S')
        if pagina_actual < total_paginas:
            console.print(Text("Presioná [ENTER] para ver la siguiente página, o [S] para volver al menú:", style="bold blue"), end="")
            opcion_pausa = input().strip().lower() 
            if opcion_pausa == 's':
                return # Salir de la función de impresión

        elif total_paginas > 1:
             console.print("\n[bold green] Fin de la lista. Presiona [ENTER] para continuar.[/bold green]", end="")
             input() # Pausa final


# --- FUNCIÓN PRINCIPAL  ---

def paises_por_continente():
    """
    Cuenta y lista países por continente, usando try-except, Rich y paginación.
    """
    # 1. Manejo de Errores (try-except) al abrir el archivo
    try:
        with open("data/paises.csv", "r", encoding="utf-8") as archivo:
            lector = list(csv.DictReader(archivo))

    except FileNotFoundError:
        console.print(f"❌ [bold red]Error:[/bold red] No se encontró el archivo [yellow]'data/paises.csv'[/yellow].", style="on red")
        return
    except Exception as e:
        console.print(f"❌ [bold red]Ocurrió un error al leer el archivo: {e}[/bold red]")
        return

    # 2. Solicitud del Continente
    continente = None
    while True:
        console.clear()
        console.print("[bold yellow]🌎 Búsqueda de países por Continente:[/bold yellow]")
        
        console.print(Text("Ingresá el nombre del continente (o deja vacío para cancelar):", style="bold blue"), end=" ")
        continente = input().strip()
        
        if not continente:
            console.print("[yellow]Búsqueda cancelada.[/yellow]")
            return

        # Filtramos los países que pertenezcan a ese continente
        datos = [fila for fila in lector if obtener_valor_seguro(fila, 'continente').lower() == continente.lower()]
        
        if datos:
            break # Continente válido, salimos del bucle
        else:
            console.print(f"❌ [bold red]Error:[/bold red] No se encontraron países en el continente '[yellow]{continente}[/yellow]'.")
            console.print("[dim white]Presioná [ENTER] para reintentar.[/dim white]", end="")
            input()
            
    # 3. Mostrar Resultado (Conteo e Impresión Paginada)
    cantidad = len(datos)

    # Imprimimos el conteo total antes de la tabla, si es necesario
    console.print(f"\n[bold green] La cantidad total de países en {continente.title()} es: [cyan]{cantidad}[/cyan].[/bold green]")
    
    # Imprimimos la lista de países en una tabla paginada
    imprimir_tabla_paginada_rich(datos, continente, cantidad, 10)
    
    # Pausa final al salir de la tabla
    console.print("\n[dim white]Presioná [ENTER] para volver al menú principal.[/dim white]", end="")
    input()

