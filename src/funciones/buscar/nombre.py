import csv
from rich.console import Console # type: ignore
from rich.table import Table # type: ignore
from rich.panel import Panel # type: ignore
from rich.box import HEAVY# type: ignore


def buscar_pais():
    console= Console()
    buscar_nombre: str=str(input("ingrese nombre del pais (completo/parcial) "))
    console.clear()
    if not buscar_nombre: # Si el usuario no ingresa nada
        console.print(":warning: [bold red]¡ERROR![/bold red] Debe ingresar al menos un nombre o parte de él.")
    try:
        with open("data/paises.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            datos_paises = list(lector) # Carga todo el CSV en una lista
    except FileNotFoundError:
        console.print(Panel("Archivo [bold red]data/paises.csv[/bold red] no encontrado.", title="[bold red]Error de Archivo[/bold red]"))
        return    
   
    nombre_normalizado = buscar_nombre.lower()
    resultados = []
    
    for fila in datos_paises:
        nombre_pais_normalizado = fila['nombre'].lower()
        
     
        if nombre_pais_normalizado == nombre_normalizado:    # Busca la coincidencia COMPLETA
            resultados = [fila] 
            break # Si está el país completo, sale del bucle sale del ciclo
        
        
        elif nombre_normalizado in nombre_pais_normalizado: # Coincidencia parcial
            if len(nombre_normalizado) >= 3:
                resultados.append(fila)

  
    if resultados: # Usamos Panel para mostrar el título y hacer la presentación más elegante
        titulo = f"[bold white on blue]Resultados para '{buscar_nombre}'[/bold white on blue]"
        console.print(Panel(
            "\n".join([
                f"[bold red]Nombre:[/bold red] [green]{r['nombre']}[/green] | "
                f"[bold blue]Población:[/bold blue] [yellow]{r['poblacion']}[/yellow] | "
                f"[bold blue]Continente:[/bold blue] [yellow]{r['continente']}[/yellow]"
                for r in resultados
            ]),
            title=titulo,
            border_style="cyan"
        ))
    else:
        # Mensaje de no encontrado usando console.print y estilos
        console.print(f"No se encontró el país '[bold magenta]{buscar_nombre}[/bold magenta]'", style="bold on red")
    
    """# Abrimos el CSV
    with open("data/paises.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)  # convierte cada fila en un diccionario
## acá usar el try excep
        #buscamos coincidencia completa
        for fila in lector:
            if fila['nombre'].lower() == buscar_nombre.lower():  
                # Si coincide, imprimimos todos los datos
                console.print(f"[bold red]Nombre:[/bold red] [green]{fila['nombre']}[/green]")
                console.print(f"[bold blue]Población:[/bold blue] [yellow]{fila['poblacion']}[/yellow]")
                console. print(f"[bold blue]Superficie:[/bold blue] [yellow]{fila['superficie']}[/yellow]")
                console.print(f"[bold blue]Continente:[/bold blue] [yellow] {fila['continente']}[/yellow]")
                return  
            #buscamos coincidencia parcial (primeras 3 letras)
            elif fila['nombre'][:3].lower() == buscar_nombre[:3].lower(): 
                # Si coincide, imprimimos todos los datos
                console.print(f"[bold red]Nombre:[/bold red] [green]{fila['nombre']}[/green]")
                console.print(f"[bold blue]Población:[/bold blue] [yellow]{fila['poblacion']}[/yellow]")
                console. print(f"[bold blue]Superficie:[/bold blue] [yellow]{fila['superficie']}[/yellow]")
                console.print(f"[bold blue]Continente:[/bold blue] [yellow] {fila['continente']}[/yellow]")
                return

        
        console.print(f"[bold red]No se encontró el país '{buscar_nombre}'[/bold red]")


## Sugerencia:
"""