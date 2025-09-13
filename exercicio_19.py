
'''19. Crie uma lista de 10 números. Use um laço for para calcular a média dos 
números pares.''' 

numList = [2,4,5,8,1,7,9,3,6,10]

soma = 0 # soma dos números pares

numPar = [] # números pares

for n in numList:

    if n % 2 == 0:
        numPar.append(n)
        soma += n
        
count = len(numPar) # quantidade de itens com número par
average = soma / count

        
print(numPar)
print(soma)
print(average)


