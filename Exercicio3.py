notas = [8,7,9,10,4,5,9,]

total_aprovados = 0

for nota in notas:
    if nota >= 7:
        total_aprovados += 1
print("Total de notas maiores ou iguais a 7:", total_aprovados)