estoque = {
    "Batata": 20,
    "Leite": 8,
    "Trigo": 7,
    "Filé de Frango": 11,
    "Iogurte": 6
}

for produto, quantidade in estoque.items():
    if quantidade < 10:
        print(f"Estoque baixo! Produto: {produto}")