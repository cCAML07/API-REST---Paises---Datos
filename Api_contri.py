import requests as requests

def listar_nombre_paises(url):
    paises = requests.get(url)
    paises = paises.json()

    for pais in paises:
          print(f"Nombre Oficial en Español:{pais['translations']['spa']['official']}")
          print(f"Capital:{pais['capital'][0]}")
          print(f"Codigo telf:{pais['idd']['root'] + pais['idd']['suffixes'][0]}")

          if "currencies" in pais:
              for codigo , info in pais["currencies"].items():
                  nombre = info["name"]
                  print(f"Tipo de moneda ({codigo}):{nombre}")


url = 'https://restcountries.com/v3.1/independent?=status=true&fields=translations,capital,idd,currencies'
listar_nombre_paises(url)
