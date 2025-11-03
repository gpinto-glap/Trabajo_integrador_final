🌍 Proyecto Integrador UTN
📝 Descripción general

Este proyecto consiste en una aplicación desarrollada en Python 3 que permite gestionar y analizar información de países a partir de un archivo CSV.
El programa fue diseñado aplicando principios de programación modular, utilizando listas, diccionarios y funciones para mantener un código claro, ordenado y fácil de mantener.

A través de un menú interactivo en consola, el usuario puede:

Buscar países por nombre.

Filtrar datos según distintos criterios (como continente, población o superficie).

Ordenar los resultados por diferentes campos.

Obtener estadísticas como el país con mayor o menor población, promedios de superficie y cantidad de países por continente.

Todo el procesamiento se realiza directamente sobre el archivo CSV, con validaciones que evitan errores comunes y garantizan una experiencia simple y fluida.

El objetivo principal de este trabajo es poner en práctica los fundamentos de la programación estructurada, trabajando con estructuras de datos, condicionales, bucles, manejo de archivos y generación de estadísticas básicas.

⚙️ Instrucciones de ejecución

El programa puede ejecutarse de manera local o mediante Docker, según la preferencia del usuario.

🔸 Ejecución local

Clonar o descargar el repositorio:

git clone <URL-del-repo>


Verificar que esté instalado Python 3.x.

Ejecutar el programa principal desde la terminal o IDE:

python main.py

🐳 Ejecución con Docker

Abrir una terminal en la carpeta raíz del proyecto.

Construir la imagen con:

docker build -t nombre_imagen .


Ejecutar el contenedor con:

docker run -it --rm -v ${PWD}:/app nombre_imagen

💡 Ejemplo de funcionamiento


---------------------------------------------------
1) Buscar país por nombre
2) Filtrar paises
3) Ordenar paises
4) Estadísticas
5) Salir


Ejemplo de búsqueda:

🔍 Ingrese el nombre del país a buscar o escriba 'exit' para volver al menú anterior.

IMPORTANTE: Las entradas deben ser en ingles. Por ejemplo

# nombre de país: Turkey
# nombre de continente: South America



👥 Integrantes

DUCI MAXIMO

PINTO GUILLERMO
