cidades = {
    "Guaratinguetá": 12300000,
    "Lorena": 6748000,
    "Cunha": 1949000,
    "Campos do Jordão": 1214000,
    "Piquete": 361855
}

for cidade, populacao in cidades.items():
    if populacao > 1_000_000:
        print(cidade)