paises = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "França": "Paris",
    "Japão": "Tóquio",
    "Austrália": "Camberra"
}

for pais, capital in paises.items():
    if pais == "Brasil":
        print("A capital do Brasil é:", capital)
        break