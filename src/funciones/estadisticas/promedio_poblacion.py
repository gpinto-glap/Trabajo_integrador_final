import csv
import sys
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.style import Style
from rich.table import Table

# Inicializa la consola de Rich
console = Console()

# --- FUNCIONES AUXILIARES  ---

def formato_numero_rich(numero: float) -> str:
    """Formatea un número flotante o entero grande con separadores de miles y color azul."""
    # El :,.0f formatea el número con separadores de miles y sin decimales
    return f"[cyan]{numero:,.0f}[/cyan]".replace(",", " ") 

def obtener_poblacion_segura(fila):
    """
    Obtiene el valor de la población como int para el cálculo.
    Devuelve 0 si el valor es inválido o no existe.
    """
    valor = fila.get('poblacion', "0")
    try:
        return int(valor)
    except (ValueError, TypeError):
        return 0 # Ignorar datos malos en la suma

# --- FUNCIÓN PRINCIPAL REESCRITA ---

def promedio_poblacion():
    """
    Calcula y muestra el promedio de población, con opción de filtrar por continente.
    Usa Rich para la presentación y try-except para manejo de archivos.
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
    
    # 2. Solicitud de Filtro por Continente (Usando input() y validación)
    
    # Bucle para validar la entrada 's' o 'n'
    while True:
        console.clear()
        console.print("[bold yellow]🌍 Cálculo de Promedio de Población:[/bold yellow]")
        console.print(Text("¿Querés calcular el promedio solo de un continente? (s/n):", style="bold white"), end=" ")
        filtro = input().strip().lower()

        if filtro in ('s', 'n', ''):
            if filtro == '': # Tratar Enter como 's' para simplificar, o 'n'  : solo valida s/n.
                filtro = 'n'
            break
        else:
            console.print("❌ [bold red]Opción no válida.[/bold red] Por favor, elegí 's' o 'n'.")
            console.print("[dim white]Presioná [ENTER] para reintentar.[/dim white]", end="")
            input()
    
    datos = lector # Inicialmente, todos los datos
    continente = None

    # 3. Filtrado y Manejo de Errores de Filtro
    if filtro == 's':
        while True:
            console.clear()
            console.print("[bold yellow]🌍 Cálculo de Promedio de Población:[/bold yellow]")
            console.print(Text("Ingresá el continente (o deja vacío para cancelar):", style="bold blue"), end=" ")
            continente_input = input().strip()

            if not continente_input:
                console.print("[yellow]Filtro cancelado. Volviendo al menú principal.[/yellow]")
                return

            continente = continente_input.lower()
            
            # Filtramos los países que coincidan con el continente
            datos_filtrados = [fila for fila in lector if fila.get('continente', '').lower() == continente]
            
            if datos_filtrados:
                datos = datos_filtrados
                break # Continente válido
            else:
                console.print(f"❌ [bold red]Error:[/bold red] No se encontraron países en el continente '[yellow]{continente.title()}[/yellow]'.")
                console.print("[dim white]Presioná [ENTER] para reintentar.[/dim white]", end="")
                input()
    
    # 4. Cálculo del Promedio (Usando la función segura)
    if not datos:
        # Esto ocurre si el archivo está vacío o si datos_filtrados quedó vacío (lo cual ya manejamos, pero como doble seguridad)
        console.print("[bold yellow]⚠️ No hay datos válidos para calcular el promedio.[/bold yellow]")
        input("Presioná [ENTER] para volver.")
        return

    total_poblacion = sum(obtener_poblacion_segura(fila) for fila in datos)
    cantidad_paises = len(datos)
    
    # Se debe verificar que la cantidad de países sea mayor a cero para evitar división por cero
    if cantidad_paises > 0:
        promedio = total_poblacion / cantidad_paises
    else:
        # En caso de que todos los datos tengan población inválida (pero el continente existiera)
        promedio = 0 


    # 5. Mostrar el Resultado en un Panel de Rich
    
    if filtro == 's' and continente:
        titulo = f"PROMEDIO DE POBLACIÓN EN {continente.upper()}"
        resumen_paises = f"Basado en {cantidad_paises} países."
    else:
        titulo = "PROMEDIO GLOBAL DE POBLACIÓN"
        resumen_paises = f"Basado en un total de {cantidad_paises} países."
        
    promedio_formateado = formato_numero_rich(promedio)

    console.clear()
    
    # Crear la tabla de resultados para un mejor formato
    resultado_table = Table(
        title=titulo,
        title_style="bold yellow",
        show_header=False,
        border_style="green"
    )
    resultado_table.add_column("Detalle", style="bold magenta", justify="left")
    resultado_table.add_column("Valor", justify="right")
    
    resultado_table.add_row(
        Text("Población Total Sumada:", style="white"),
        formato_numero_rich(total_poblacion)
    )
    resultado_table.add_row(
        Text("Número de Países Analizados:", style="white"),
        f"[cyan]{cantidad_paises}[/cyan]"
    )
    resultado_table.add_row(
        Text("Promedio Calculado:", style="bold white"),
        promedio_formateado
    )

    console.print(resultado_table)

    # Pausa final
    console.print("\n[bold green] Cálculo completado.[/bold green]")
    console.print("[dim white]Presioná [ENTER] para volver al menú.[/dim white]", end="")
    input()

