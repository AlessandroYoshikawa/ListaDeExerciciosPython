numeros = [10, -3, 7, -8, 15, -2, -11, 5, 20, -6]

soma_negativos = 0

for numero in numeros:
    if numero < 0:
        soma_negativos += numero

print("A soma dos números negativos é:", soma_negativos)