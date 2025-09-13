frutas = {
    "Maçã": "Vermelha",
    "Banana": "Amarela",
    "Laranja": "Laranja",
    "Uva": "Roxa",
    "Abacaxi": "Amarela"
}

nova_fruta = input("Digite o nome da fruta que deseja adicionar: ")
cor_fruta = input("Digite a cor da fruta: ")

frutas[nova_fruta] = cor_fruta

print("Dicionário atualizado:")
for fruta, cor in frutas.items():
    print(f"{fruta}: {cor}")