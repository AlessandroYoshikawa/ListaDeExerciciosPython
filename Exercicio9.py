numeros = [12, 45, 7, 89, 23, 56, 91, 34, 67, 10]

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero

print("O menor número da lista é:", menor)