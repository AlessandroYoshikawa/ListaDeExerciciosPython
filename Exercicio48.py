produto = {"nome": "Notebook", "preço": 3500.0, "disponível": True}

nome_usuario = input("Digite o nome do produto que deseja verificar: ")

for chave, valor in produto.items():
    if chave == "nome":
        if nome_usuario == valor:
            if produto["disponível"]:
                print(f"O produto {valor} está disponível!")
            else:
                print(f"O produto {valor} não está disponível!")
        else:
            print(f"O produto {nome_usuario} não existe na loja!")
