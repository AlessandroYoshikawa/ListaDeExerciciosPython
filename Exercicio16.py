lista_numeros = [12, 7, 25, 40, 18, 33, 2, 9, 50, 61]

pares = []
impares = []

for num in lista_numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista original:", lista_numeros)
print("Números pares:", pares)
print("Números ímpares:", impares)