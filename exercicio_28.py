
''' 28. Crie uma lista de 10 números. Use um laço for para imprimir os números em 
ordem decrescente. '''


a = [1, 2, 4, 5, 7, 8, 10, 9, 14, 20]

b = len(a) # números em ordem decrescente

for i in range(b):
    for j in range( 0, b - i - 1):
        if a[j] < a[j + 1]:
            a[j], a [j + 1] = a[j + 1], a[j]
            
for number in a:
    print(number)
    

