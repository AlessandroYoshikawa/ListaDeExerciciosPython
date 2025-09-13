lista_palavras = ["casa", "computador", "universo", "amigo", "linguagem"]

vogais = "aeiouAEIOU"

total_vogais = 0

for palavra in lista_palavras:
    for letra in palavra:
        if letra in vogais:
            total_vogais += 1

print("Lista de palavras:", lista_palavras)
print("Total de vogais em todas as palavras:", total_vogais)