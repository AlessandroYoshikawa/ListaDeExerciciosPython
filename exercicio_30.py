
''' 30. Crie uma lista de strings. Use um laço for para contar a quantidade de strings 
que começam com a letra 'P'. ''' 


a = ["parafuso", "casa", "pipa", "joia", "bola", "árvore"]

stringP = 0 # Strings com a letra "p"

for i in a:
    if i.startswith('p'):
        stringP += 1
        
print(stringP)



