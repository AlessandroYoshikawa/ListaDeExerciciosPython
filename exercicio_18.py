
''' 18. Dada uma lista com 15 números, use um laço for para remover todas as 
duplicatas. Ao final, imprima a lista com apenas valores únicos. '''

numeros = [1, 2, 3, 4, 1, 4, 5, 8, 7, 9, 10, 11, 7, 8, 9]

semRepeticao = [] # sem duplicatas

for n in numeros:
    semRepeticao = list(set(numeros))
    
print(semRepeticao)


