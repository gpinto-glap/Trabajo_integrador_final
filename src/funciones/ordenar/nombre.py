import csv
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Inicializamos la consola de rich
console = Console()

def ordenar_nombre():
    console.clear()
    
    try:# Abrimos el CSV y leemos todas las filas
        with open("data/paises.csv", "r", encoding="utf-8") as archivo:
            lector = list(csv.DictReader(archivo))
    except FileNotFoundError:
        console.print("[bold red]ERROR:[/bold red] No se encontró el archivo 'data/paises.csv' ")
        return
    except Exception as e:
        console.print(f"[bold red]ERROR al leer el archivo:[/bold red] {e}")
        return

    # Preguntamos al usuario cómo quiere ordenar
    console.print("\n[bold cyan]Opciones de orden por nombre:[/bold cyan]")
    console.print("1 - De la [blue]A[/blue] a la [blue]Z[/blue] (ascendente)")# agregar las flechas arriba y abajo
    console.print("2 - De la [orange]Z[/orange] a la [orange]A[/orange] (descendente)")
    opcion = input("Elegí una opción (1/2): ").strip()

    ordenado = []
    if opcion == "1":
        ordenado = sorted(lector, key=lambda fila: fila['nombre'])
        titulo_orden = "A a Z"
    elif opcion == "2":
        ordenado = sorted(lector, key=lambda fila: fila['nombre'], reverse=True)
        titulo_orden = "Z a A"
    else:
        # Si la opción es inválida mostramos el error
        console.print("[bold yellow]Opción inválida[/bold yellow]")
        input("presiona ENTER para continuar ")
        return
#paginación
    paises_por_pagina = 10  # Número de filas por página
    total_paginas = (len(ordenado) + paises_por_pagina - 1) // paises_por_pagina
    pagina_actual = 1

    while True:
        console.clear() 
        inicio = (pagina_actual - 1) * paises_por_pagina
        fin = inicio + paises_por_pagina
        paises_pagina = ordenado[inicio:fin]
        
        #Crear la tabla
        tabla = Table(title=f"Países ordenados de {titulo_orden} ({len(ordenado)} en total)\n[bold yellow]Página {pagina_actual}/{total_paginas}[/bold yellow]", show_lines=True)

        #Definir columnas
        tabla.add_column("Nombre", style="bold yellow", justify="left")
        tabla.add_column("Población", style="magenta", justify="right")
        tabla.add_column("Superficie (km²)", style="cyan", justify="right")
        tabla.add_column("Continente", style="green", justify="left")

        # Llenar la tabla con datos
        for fila in paises_pagina:
            nombre = fila['nombre']
            # Formato con separador
            poblacion = f"{int(fila['poblacion']):,}".replace(",", ".") 
            superficie = f"{int(fila['superficie']):,}".replace(",", ".") 
            continente = fila['continente']
            
            
            tabla.add_row(
                Text(nombre, style="bold yellow"), 
                Text(poblacion, style="magenta"),      
                Text(superficie, style="cyan"),       
                Text(continente, style="green"),
            )
        # Imprimir la tabla
        console.print(tabla)
        if total_paginas <= 1:#Lógica de paginación
            break

        print("\n" + "=" * 50)
        
        if pagina_actual < total_paginas:
            opciones = "[bold]ENTER[/bold] - Siguiente página | [bold]S[/bold] - Salir"
            mensaje_input = "Presiona ENTER para continuar o S para salir: "
        else: # Última página
            opciones = "[bold]S[/bold] - Salir"
            mensaje_input = "Presiona S para salir: "
        
        console.print("[green]Opciones:[/green]  " + opciones)
        
        accion = input(mensaje_input).strip().upper()

        if accion == 'S':
            console.clear()
            console.print("\n[bold yellow]Saliendo de la paginación.[/bold yellow]")
            break
        elif accion == '' or accion == '\n': # ENTER se detecta como una cadena vacía ('')
            if pagina_actual < total_paginas:
                pagina_actual += 1
                continue # Continúa al siguiente ciclo (próxima página)
            else:
                # Si está en la última página y presiona Enter, lo ignoramos o mostramos un mensaje.
                console.print("[bold red]Estás en la última página.[/bold red]")
                input("Presiona [Enter] para continuar...")
                continue
        else:
            # Opción no válida (no es S ni Enter)
            console.print("[yellow]:warning-text:[/yellow] [bold red] OPCION INVALIDA [/bold red] [yellow]:warning-text:[/yellow]")
            input("Presiona [Enter] para continuar...")
            continue