import csv
import sys
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.style import Style

# Inicializa la consola de Rich
console = Console()

# --- FUNCIONES AUXILIARES (Reutilizadas de la lógica anterior) ---

def formato_numero_rich(numero: str, style_color: str) -> str:
    """Formatea un número con separadores de miles y color usando Text de Rich."""
    try:
        num = int(numero)
        # Formato de número con separadores de miles
        return f"[{style_color}]{num:,.0f}[/]".replace(",", ".") 
    except (ValueError, TypeError):
        return f"[bold red]{numero}[/bold red]" # En caso de error, muestra el valor en rojo

def obtener_valor_seguro(fila, clave):
    """Obtiene el valor de la clave, manejando posibles ausencias o errores."""
    valor = fila.get(clave, "N/A")
    # Para la clave 'superficie', intentamos convertir a int para el ordenamiento
    if clave == 'superficie':
        try:
            return int(valor)
        except (ValueError, TypeError):
            return 0  # Devuelve 0 para que no falle el ordenamiento
    return valor

def imprimir_tabla_paginada_rich(data, titulo, elementos_por_pagina=10):
    """Imprime los datos paginados en formato de tabla colorida de Rich."""
    
    total_elementos = len(data)
    total_paginas = (total_elementos + elementos_por_pagina - 1) // elementos_por_pagina
    
    # Definición de estilos para las columnas
    estilos_datos = [
        Style(color="cyan"),      # Nombre
        Style(color="yellow"),    # Población
        Style(color="green"),     # Superficie
        Style(color="magenta")    # Continente
    ]
    encabezados = ['Nombre', 'Población', 'Superficie', 'Continente']
    
    for pagina_indice in range(0, total_elementos, elementos_por_pagina):
        pagina_actual = (pagina_indice // elementos_por_pagina) + 1
        elementos_pagina = data[pagina_indice:pagina_indice + elementos_por_pagina]
        
        # 1. Crear la Tabla
        table = Table(
            title=titulo, 
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
                justify="right" if encabezado != 'Nombre' and encabezado != 'Continente' else "left"
            )

        # 3. Agregar Filas
        for i, fila in enumerate(elementos_pagina):
            
            # Formatear la población y superficie con separadores de miles y color
            poblacion = formato_numero_rich(obtener_valor_seguro(fila, 'poblacion'), 'yellow')
            superficie = formato_numero_rich(obtener_valor_seguro(fila, 'superficie'), 'green')
            
            # Aplicar un estilo diferente al nombre para distinguir filas
            nombre_pais = Text(obtener_valor_seguro(fila, 'nombre'), style="bold cyan")

            table.add_row(
                nombre_pais, 
                poblacion,
                superficie,
                obtener_valor_seguro(fila, 'continente')
            )

        # 4. Imprimir la información de la página y la tabla
        console.clear()
        
        # Panel para el título general y la paginación
        console.print(Panel(
            f"Página [bold magenta]{pagina_actual}[/bold magenta] de [bold magenta]{total_paginas}[/bold magenta]", 
            title="🌎 Listado de Países Ordenados por Superficie",
            title_align="left",
            border_style="magenta"
        ))
        
        console.print(table)
        
        # 5. Pausa si no es la última página (Con opción de Salir 'S')
        if pagina_actual < total_paginas:
            # Opción para Salir (S) o Continuar (ENTER)
            console.print(Text("Presioná [ENTER] para ver la siguiente página, o [S] para volver al menú:", style="bold blue"), end="")
            
            opcion_pausa = input().strip().lower() 
            
            # Verificar si el usuario desea salir (s o S)
            if opcion_pausa == 's':
                return 

        elif total_paginas > 1:
             console.print("\n[bold green]✅ Fin de la lista. Presiona [ENTER] para continuar.[/bold green]", end="")
             input() # Pausa final


# --- FUNCIÓN PRINCIPAL REESCRITA ---

def ordenar_superficie():
    """
    Lee datos de países, ordena por superficie según la elección del usuario
    e imprime los resultados en una tabla paginada con diseño Rich.
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

    # 2. Solicitud de Opción con input() y validación (Sin Prompt.ask)
    ordenado = []
    titulo_tabla = ""
    
    while True:
        console.clear()
        
        console.print("[bold yellow]🌍 Opciones de orden por superficie:[/bold yellow]")
        console.print("  [green]1[/green] - De menor a mayor superficie")
        console.print("  [green]2[/green] - De mayor a menor superficie")
        
        console.print(Text("Elegí una opción (1/2):", style="bold blue"), end=" ")
        opcion = input().strip()
        
        if opcion in ("1", "2"):
            break
        else:
            console.print("❌ [bold red]Opción no válida.[/bold red] Por favor, elegí '1' o '2'.")
            console.print("[dim white]Presioná [ENTER] para reintentar.[/dim white]", end="")
            input() 
            
    # 3. Ordenamiento
    if opcion == "1":
        # Orden ascendente por superficie, usando la función segura
        ordenado = sorted(lector, key=lambda fila: obtener_valor_seguro(fila, 'superficie'))
        titulo_tabla = "Países Ordenados por Superficie (Menor a Mayor)"
    elif opcion == "2":
        # Orden descendente por superficie, usando la función segura
        ordenado = sorted(lector, key=lambda fila: obtener_valor_seguro(fila, 'superficie'), reverse=True)
        titulo_tabla = "Países Ordenados por Superficie (Mayor a Menor)"
    
    # 4. Impresión de la Tabla Paginada
    if ordenado:
        imprimir_tabla_paginada_rich(ordenado, titulo_tabla, 10)
    else:
        console.print("[bold yellow]⚠️ No hay datos para mostrar.[/bold yellow]")



"""import csv

def ordenar_superficie(): #FALTA TRY EXCEPT
    # Abrimos el CSV y leemos todas las filas
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = list(csv.DictReader(archivo))

    # Preguntamos al usuario cómo quiere ordenar
    print("Opciones de orden por superficie:")
    print("1 - De menor a mayor superficie")
    print("2 - De mayor a menor superficie")
    opcion = input("Elegí una opción (1/2): ").strip()

    if opcion == "1":
        # Orden ascendente por superficie
        ordenado = sorted(lector, key=lambda fila: int(fila['superficie']))
    elif opcion == "2":
        # Orden descendente por superficie
        ordenado = sorted(lector, key=lambda fila: int(fila['superficie']), reverse=True)
    else:
        print("Opción inválida")
        return

    # Imprimir todos los países ordenados
    for fila in ordenado:
        print(f"Nombre: {fila['nombre']}, Población: {fila['poblacion']}, Superficie: {fila['superficie']}, Continente: {fila['continente']}")"""
