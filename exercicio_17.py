
''' 17. Crie uma lista de 5 palavras. Use um laço for para criar uma nova lista que 
contenha as palavras ao contrário. '''


palavras = ["teclado", "alegria", "estudar", "gentil", "hoje"]
oppositeWords = [] # palavras ao contrário

for w in palavras:
    oppositeWords.insert(0, w)
        
print(f"Palavras: {palavras}")
print(f"Palavras ao Contrário: {oppositeWords}")

