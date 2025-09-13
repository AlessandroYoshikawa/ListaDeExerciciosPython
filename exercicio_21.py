
''' 21. Crie uma lista de 5 nomes de pessoas. Use um laço for para criar uma nova lista 
que contenha apenas os nomes com mais de 5 letras. '''

nomes = ["Marcos", "Jose", "Ana", "Mariana", "Junior"]

n5 = []  # nomes com mais de 5 letras 

for i in nomes:
    if len(i) > 5:
        n5.append(i)

print(n5)

