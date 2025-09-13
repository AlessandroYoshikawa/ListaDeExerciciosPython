hobbies_das_pessoas = {
    "Matilda": ["leitura", "natação", "yoga", "cinema"],
    "Bruno": ["futebol", "video game", "aposta"],
    "Carmem": ["leitura", "pintura", "cozinhar"],
    "Theodoro": ["corrida", "musculação", "pilates"],
    "Eduarda": ["dança", "leitura", "dormir"]
}

for pessoa, hobbies in hobbies_das_pessoas.items():
    if "leitura" in hobbies:
        print(f"{pessoa} gosta de leitura")