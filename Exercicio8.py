numeros = [12, 45, 7, 89, 23, 56, 91, 34, 67, 10]

maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("O maior número da lista é:", maior)