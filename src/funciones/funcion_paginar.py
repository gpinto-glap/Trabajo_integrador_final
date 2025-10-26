from rich.console import Console 
from rich.table import Table 
from rich.panel import Panel 
import math

def paginar_tabla(items, encabezado, titulo="", items_por_pagina=15):
    
    #Muestra una tabla paginada en consola usando Rich.
    #items: lista de listas con los datos a mostrar
    #encabezado: lista con nombres de columnas
    #titulo: título que se mostrará en la tabla
    #items_por_pagina: cantidad de elementos por página
    
    console = Console()
    total_paginas = math.ceil(len(items) / items_por_pagina)
    pagina_actual = 1

    def mostrar_pagina(pagina):
        inicio = (pagina - 1) * items_por_pagina
        fin = inicio + items_por_pagina
        subset = items[inicio:fin]

        tabla = Table(title=f"[cyan]{titulo}[/cyan]", style="cyan", show_lines=True)
        estilos =["yellow","magenta","green","blue"]
        for col, style in zip(encabezado, estilos):
            tabla.add_column(col.capitalize(), style=style)
        for fila in subset:
            tabla.add_row(*fila)

        console.clear()
        console.print("\n", Panel(f"Los paises encontrados son :", style="bold green", expand=False))
        console.print(tabla)
        console.print(f"Página ({pagina}/{total_paginas})")
        console.print("\nEscriba 's' para siguiente | 'a' para anterior | 'e' para salir", style="bold cyan")

    while True:
        mostrar_pagina(pagina_actual)
        opcion = console.input("→ ").strip().lower()

        if opcion == "s" and pagina_actual < total_paginas:
            pagina_actual += 1
        elif opcion == "a" and pagina_actual > 1:
            pagina_actual -= 1
        elif opcion == "e":
            break