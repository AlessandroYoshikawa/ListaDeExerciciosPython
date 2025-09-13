paises = {
    "Brasil": {"capital": "Brasília", "população": "2.996.899"},
    "Argentina": {"capital": "Buenos Aires", "população": "2.995.805"},
    "França": {"capital": "Paris", "população": "12.278.210"},
    "Japão": {"capital": "Tóquio", "população": "37.843.000"},
    "Austrália": {"capital": "Camberra", "população": "452.670"}
}

for pais, info in paises.items():
    for chave, valor in info.items():
        if chave == "capital":
            print(f"A capital de {pais} é {valor}")