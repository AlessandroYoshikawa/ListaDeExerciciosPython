
''' 20. Crie uma lista de 10 números. Use um laço for para contar quantas vezes o 
número 5 aparece na lista. '''

a = [1, 2, 6, 5, 8, 9, 5, 5, 4, 8]

b = 0 

for n in a:
    if n == 5:
        b += 1
        
print(b)

