pessoas = {"Dionísio": 18, "Giéssikah": 43, "Karlah": 33, "Charles": 18, "Kahrolinna": 40}

mais_de_30 = []

for nome, idade in pessoas.items():
    if idade > 30:
        mais_de_30.append(nome)

print("Pessoas com mais de 30 anos:", mais_de_30)
