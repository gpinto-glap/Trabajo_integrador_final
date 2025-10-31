import csv
import sys
import time
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.style import Style

# Inicializa la consola
console = Console()

# --- FUNCIONES AUXILIARES ---

def formato_numero_rich(numero: str, style_color: str) -> str:
    """Formatea un número con separadores de miles y color usando Rich."""
    try:
        num = int(numero)
        # Formato de número con separadores de miles
        return f"[{style_color}]{num:,.0f}[/]".replace(",", ".") 
    except (ValueError, TypeError):
        return f"[bold red]{numero}[/bold red]" 

def obtener_poblacion_segura(fila):
    """Obtiene el valor de la población como int para ordenamiento o 0 si es inválido."""
    valor = fila.get('poblacion', "0")
    try:
        return int(valor)
    except (ValueError, TypeError):
        return 0

# --- FUNCIÓN DE IMPRESIÓN DE TABLA ÚNICA (Adaptada para 5 resultados) ---

def imprimir_tabla_estadisticas(data, titulo):
    """Imprime un conjunto de datos en una tabla colorida de Rich."""
    
    # 1. Crear la Tabla
    table = Table(
        title=titulo, 
        show_header=True, 
        header_style="bold white on #4078c0",
        border_style="dim yellow",
        title_style="bold yellow underline"
    )

    # Definición de columnas y estilos
    estilos_datos = [
        Style(color="cyan"),      # Nombre
        Style(color="yellow"),    # Población
        Style(color="green"),     # Superficie
        Style(color="magenta")    # Continente
    ]
    encabezados = ['Nombre', 'Población', 'Superficie', 'Continente']

    # 2. Definir Columnas
    for i, encabezado in enumerate(encabezados):
        table.add_column(
            encabezado, 
            style=estilos_datos[i % len(estilos_datos)], 
            justify="right" if encabezado != 'Nombre' and encabezado != 'Continente' else "left"
        )

    # 3. Agregar Filas
    for fila in data:
        poblacion = formato_numero_rich(fila.get('poblacion', 'N/A'), 'yellow')
        superficie = formato_numero_rich(fila.get('superficie', 'N/A'), 'green')
        
        nombre_pais = Text(fila.get('nombre', 'N/A'), style="bold cyan")

        table.add_row(
            nombre_pais, 
            poblacion,
            superficie,
            fila.get('continente', 'N/A')
        )

    # 4. Imprimir la tabla y la pausa
    console.clear()
    
    console.print(Panel(
        f"[bold magenta]📊 Top {len(data)} Resultados de Población[/bold magenta]", 
        title="Estadísticas de Países",
        title_align="left",
        border_style="magenta"
    ))
    
    console.print(table)
    
    # Pausa final
    console.print("\n[bold blue]Presioná [ENTER] para volver al menú.[/bold blue]", end="")
    input()


# --- FUNCIÓN PRINCIPAL REESCRITA ---

def estadisticas_poblacion():
    """
    Calcula y muestra los 5 países con menor o mayor población, 
    con opción a filtrar por continente. Usa Rich para diseño.
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
    
    datos = lector # Inicialmente, todos los datos

    # 2. Preguntamos si quiere filtrar por continente
    console.clear()
    console.print(Text("¿Querés filtrar por continente? (s/n):", style="bold white"), end=" ")
    filtro = input().strip().lower()

    if filtro == 's':
        console.print(Text("Ingresá el continente:", style="bold yellow"), end=" ")
        continente = input().strip().lower()
        
        # Filtramos
        datos = [fila for fila in lector if fila.get('continente', '').lower() == continente]
        
        if not datos:
            console.print(f"\n[bold yellow]⚠️ No se encontraron países en el continente '{continente}'[/bold yellow]")
            input("Presioná [ENTER] para volver.")
            return

    # 3. Preguntamos la opción de estadística (Usando la lógica de validación simple)
    opcion = None
    while True:
        console.clear()
        console.print("[bold yellow]🌍 Opciones de estadística por población:[/bold yellow]")
        console.print("  [green]1[/green] - Primeros [yellow]10 países[/yellow] de menor población")
        console.print("  [green]2[/green] - Primeros [magenta]10[/magenta] países de mayor población")
        
        console.print(Text("Elegí una opción (1/2):", style="bold blue"), end=" ")
        opcion = input().strip()
        
        if opcion in ("1", "2"):
            break
        else:
            console.print("❌ [bold red]Opción no válida.[/bold red] Por favor, elegí '1' o '2'.")
            console.print("[dim white]Presioná [ENTER] para reintentar.[/dim white]", end="")
            input() 

    # 4. Ordenamiento y Obtención de Resultados (Top 10)
    resultados = []
    titulo_tabla = ""

    # Usamos la función segura para evitar errores en el sort
    if opcion == "1":
        # Orden ascendente por población y tomamos los 10 primeros
        ordenado = sorted(datos, key=obtener_poblacion_segura)
        resultados = ordenado[:10]
        titulo_tabla = "Top 10 Países con MENOR Población"
    elif opcion == "2":
        # Orden descendente por población y tomamos los 10 primeros
        ordenado = sorted(datos, key=obtener_poblacion_segura, reverse=True)
        resultados = ordenado[:10]
        titulo_tabla = "Top 10 Países con MAYOR Población"
    
    # 5. Impresión de la Tabla
    if resultados:
        imprimir_tabla_estadisticas(resultados, titulo_tabla)
    else:
        # Esto solo ocurriría si el filtro de continente dejó menos de 5 resultados 
        # y algo falló, o si el CSV estaba vacío
        console.print("[bold yellow]⚠️ No se pudieron obtener los resultados de la estadística.[/bold yellow]")
        input("Presioná [ENTER] para volver.")

"""import csv

def estadisticas_poblacion():
    # Abrimos el CSV y leemos todas las filas
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = list(csv.DictReader(archivo))

    # Preguntamos si quiere filtrar por continente
    filtro = input("¿Querés filtrar por continente? (s/n): ").strip().lower()
    if filtro == 's':
        continente = input("Ingresá el continente: ").strip().lower()
        # Filtramos solo los países que coincidan con el continente
        datos = [fila for fila in lector if fila['continente'].lower() == continente]
        if not datos:
            print(f"No se encontraron países en el continente '{continente}'")
            return
    else:
        datos = lector  # usamos todos los países

    # Preguntamos la opción de estadística
    print("Opciones de estadística por población:")
    print("1 - Primeros 5 países de menor población")
    print("2 - Primeros 5 países de mayor población")
    opcion = input("Elegí una opción (1/2): ").strip()

    if opcion == "1":
        # Orden ascendente por población y tomamos los 5 primeros
        resultados = sorted(datos, key=lambda fila: int(fila['poblacion']))[:5]
    elif opcion == "2":
        # Orden descendente por población y tomamos los 5 primeros
        resultados = sorted(datos, key=lambda fila: int(fila['poblacion']), reverse=True)[:5]
    else:
        print("Opción inválida")
        return

    # Imprimir resultados
    print("\nResultados:")
    for fila in resultados:
        print(f"Nombre: {fila['nombre']}, Población: {fila['poblacion']}, Superficie: {fila['superficie']}, Continente: {fila['continente']}")"""