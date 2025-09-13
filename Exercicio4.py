numeros=[12,8,4,9,5,20,15,28]

numeros_pares = []

for numero in numeros:
    if numero%2==0:
        numeros_pares.append(numero)
        
print("numeros pares:", numeros_pares)