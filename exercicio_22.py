
''' 22. Crie uma lista de 10 números. Use um laço for para criar uma nova lista com o 
dobro de cada número. '''


numeros = [1, 2, 4, 3, 7, 8, 5, 9, 10, 11]

n2 = []  # o dobro de cada número '''

for number in numeros:
    resultado = number * 2
    n2.append(resultado)
    
print(n2)


