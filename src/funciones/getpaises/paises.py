import requests # type: ignore

def get_paises():
    try:
        res = requests.get("https://restcountries.com/v3.1/all?fields=name,population,area,continents")
        res.raise_for_status()
        todo = res.json()
        csv = [
            "nombre,poblacion,superficie,continente\n"
    ]
 
        info = list(map(
        lambda e:  
        # el pais Saint Helena, Ascension and Tristan da Cunha me daba mal formato en el csv para hacer la tabla asi que aca lo reemplazo
        f"{'Saint Helena (Tristan da Cunha)' if e['name']['common']=='Saint Helena, Ascension and Tristan da Cunha' else e['name']['common']},{int(e['population'])},{int(round(e['area']))},{e['continents'][0]}\n",
        todo
        ))

        csv += info

    except requests.exceptions.RequestException as error:
        print("Error", error)  

    with open("data/paises.csv", "w")as archivo:
        archivo.writelines(csv)