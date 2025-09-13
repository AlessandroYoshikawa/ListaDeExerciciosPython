frase = "Lorem Ipsum is simply dummy text of the printing and typesetting industry"

frequencia = {}

for letra in frase:
    if letra != "":
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

print(frequencia)
