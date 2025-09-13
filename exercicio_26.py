
''' 26. Crie uma lista de strings. Use um laço for para remover todas as strings que 
contêm a letra 'a'. '''

a = ["a", "m", "r", "d", "q", "x", "abcd", "nadf"]

remove = [] # lista com Strings que não contêm a letra "a"

for w in a:
    if 'a' not in w:
        remove.append(w)
        
print(remove)

