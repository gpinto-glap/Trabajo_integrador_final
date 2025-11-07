import csv
from rich.console import Console # type: ignore
from rich.table import Table # type: ignore
from rich.panel import Panel # type: ignore
from rich.text import Text # type: ignore
from rich.box import HEAVY # type: ignore


def buscar_pais():
    console= Console()
    buscar_nombre: str=str(input("ingrese nombre del pais (completo/parcial) "))
    
    if not buscar_nombre: # Si el usuario no ingresa nada
        console.print(":warning: [bold red]¡ERROR![/bold red]:warning: Debe ingresar al menos un nombre o parte de él.")
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
        titulo_tabla = f"Resultados para '[bold yellow]{buscar_nombre}[/bold yellow]'"
        
        tabla = Table(title=titulo_tabla, 
                      show_header=True, 
                      header_style="bold cyan", 
                      box=HEAVY)

        # Definir Columnas y estilos para alineación perfecta
        tabla.add_column("Nombre", style="green", justify="left")
        tabla.add_column("Población", style="magenta", justify="right")
        tabla.add_column("superficie", style="magenta", justify="right")
        tabla.add_column("Continente", style="yellow", justify="left")
        
        # Llenar la tabla
        for r in resultados:
            # Uso de Text y formato para separar miles (replicando el patrón de otras funciones)
            poblacion_formateada = f"{int(r.get('poblacion', 0)):,}".replace(",", ".")
            superficie_formateada = f"{int(r.get('superficie', 0)):,}".replace(",", ".")

            tabla.add_row(
                Text(r['nombre'], style="green"),
                Text(poblacion_formateada, style="magenta"),
                Text(superficie_formateada, style="blue"),
                Text(r['continente'], style="yellow"),
            )

        # Imprimir la tabla completa
        console.print(tabla)
    else:
        # Mensaje de no encontrado usando console.print y estilos
        console.print(f"No se encontró el país '[bold magenta]{buscar_nombre}[/bold magenta]'", style="bold on red")
    input("\nPresiona [Enter] para continuar...")
#llamada a la funcion para probar
#buscar_pais()
