
''' 27. Crie uma lista de 10 números. Use um laço for para encontrar a mediana da 
lista (após ordená-la). '''

a = [2, 20, 30, 12, 14, 15, 17, 23, 28, 30]

n = len(a)

for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            
print(a)

middle_index1 = len(a) // 2
middle_index2 = middle_index1 - 1

middle_value1 = a[middle_index1] 
middle_value2 = a[middle_index2] 

print(f" {middle_value1} and {middle_value2}")



