

''' 31. Crie um dicionário com 3 nomes de cidades e seus respectivos estados. Use um 
laço for para imprimir cada par de chave e valor. ''' 

cities_and_states = {
    "São Paulo": "São Paulo",
    "Rio de Janeiro": "Rio de Janeiro",
    "Salvador": "Bahia"
}

for city, state in cities_and_states.items():

    print(f"The city is {city}, and the state is {state}.")


