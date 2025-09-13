livros = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"titulo": "A Moreninha", "autor": "Joaquim Manuel de Macedo"},
    {"titulo": "Quincas Borbas", "autor": "Machado de Assis"},
    {"titulo": "Iracema", "autor": "José de Alencar"},
    {"titulo": "O Alienista", "autor": "Machado de Assis"}
]

for livro in livros:
    if livro["autor"] == "Machado de Assis":
        print(livro["titulo"])