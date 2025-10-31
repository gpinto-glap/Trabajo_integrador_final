import csv
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
console=Console()

def buscar_superficie():
    console.clear()
    try:
        with open("data/paises.csv", "r", encoding="utf-8") as archivo:
            lector = list(csv.DictReader(archivo)) 
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] No se encontró 'data/paises.csv'.")
        input("Presiona [Enter] para volver al menú...")
        return
    except Exception as e:
        console.print(f"[bold red]Error al leer el archivo:[/bold red] {e}")
        input("Presiona [Enter] para volver al menú...")
        return

    # Menú de opciones
    console.print("\n[bold cyan]Opciones de búsqueda por superficie:[/bold cyan]")
    console.print("1 - Paises con superficie [bold blue]MAYOR[/bold blue] a un número")
    console.print("2 - Paises con superficie [bold magenta]MENOR[/bold magenta] a un número")
    console.print("3 - Paises con superficie [yellow]entre[/yellow] dos números")
    opcion = input("Elegí una opción (1/2/3): ")
    
    resultados = []
    criterio = "" # Para el título de la tabla
    try:
        if opcion == "1":
            numero = int(input("Ingresá el número mínimo de superficie: "))
            resultados = [fila for fila in lector if int(fila['superficie']) > numero]
            criterio = f"Superficie > {numero:,}".replace(",", ".")

        elif opcion == "2":
            numero = int(input("Ingresá el número máximo de superficie: "))
            resultados = [fila for fila in lector if int(fila['superficie']) < numero]
            criterio = f"Superficie < {numero:,}".replace(",", ".")

        elif opcion == "3":
            min_num = int(input("Ingresá el número mínimo de superficie: "))
            max_num = int(input("Ingresá el número máximo de superficie: "))
            resultados = [fila for fila in lector if min_num <= int(fila['superficie']) <= max_num]
            criterio = f"Superficie entre {min_num:,} y {max_num:,}".replace(",", ".")

        else:
            console.print(":warning: [bold yellow] Opción inválida[/bold yellow] :warning:")
            input("Presiona [Enter] para continuar...")
            return
            
    except ValueError:
        console.print(":warning:[bold red]Error:[/bold red] :warning Debes ingresar un número válido.")
        input("Presiona [Enter] para continuar...")
        return

    # resultados
    if not resultados:
        console.clear()
        console.print(f"[bold yellow]No se encontraron países[/bold yellow] que cumplan el criterio: [cyan]{criterio}[/cyan]")
        input("Presiona [Enter] para continuar...")
        return

    paises_por_pagina = 10
    total_paginas = (len(resultados) + paises_por_pagina - 1) // paises_por_pagina
    pagina_actual = 1
    while True:
       
        console.clear() 

        inicio = (pagina_actual - 1) * paises_por_pagina
        fin = inicio + paises_por_pagina
        paises_pagina = resultados[inicio:fin]
        
        # Crear tabla con título y criterio
        tabla = Table(title=f"Resultados de Búsqueda ({len(resultados)} países)\n[bold cyan]{criterio}[/bold cyan] | Página {pagina_actual}/{total_paginas}", show_lines=True)

        tabla.add_column("Nombre", style="bold yellow", justify="left")
        tabla.add_column("Población", style="magenta", justify="right")
        tabla.add_column("Superficie (km²)", style="cyan", justify="right")
        tabla.add_column("Continente", style="green", justify="left")

        # Llenar la tabla con datos y colores de columna
        for fila in paises_pagina:
            nombre = fila['nombre']
            # Formato con separador 
            poblacion = f"{int(fila['poblacion']):,}".replace(",", ".") 
            superficie = f"{int(fila['superficie']):,}".replace(",", ".") 
            continente = fila['continente']
            
            # Aplicar estilos por columna 
            tabla.add_row(
                Text(nombre, style="bold yellow"),
                Text(poblacion, style="magenta"),
                Text(superficie, style="cyan"),
                Text(continente, style="green"),
            )
        console.print(tabla)

        # Lógica de Paginación (Avanzar con ENTER)
        if total_paginas <= 1:
            break

        print("\n" + "=" * 50)
        
        # Opciones mostradas al usuario
        if pagina_actual < total_paginas:
            opciones = "[bold]ENTER[/bold] - Siguiente página | [bold]S[/bold] - Salir"
            mensaje_input = "Presiona ENTER para continuar o S para salir: "
        else: # Última página
            opciones = "[bold]S[/bold] - Salir"
            mensaje_input = "Presiona S para salir: "
        
        console.print("Opciones: " + opciones)
        
        accion = input(mensaje_input).strip().upper()

        if accion == 'S':
            break
        elif accion == '' or accion == '\n': # ENTER se detecta como una cadena vacía ('')
            if pagina_actual < total_paginas:
                pagina_actual += 1
                continue 
            else:
                console.print("[bold red]Estás en la última página.[/bold red]")
                input("Presiona [Enter] para continuar...")
                continue
        else:
            console.print(":warning:[bold yellow] Opción inválida.[/bold yellow] :warning:")
            input("Presiona [Enter] para continuar...")
            continue
            
    # Limpia al salir del bucle
    console.clear()
   