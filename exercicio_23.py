
''' 23. Crie duas listas de 5 números cada. Use laços for aninhados para multiplicar 
cada número da primeira lista por cada número da segunda lista. '''

a = [0, 2, 5, 7, 9]
b = [3, 4, 6, 8, 1]

for n1 in a:
    for n2 in b:
        resultado = n1 * n2
        print(f"{n1} * {n2} = {resultado}")


