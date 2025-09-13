

''' 32. Crie um dicionário para um estudante, com as chaves: nome, idade, curso e 
notas. Use um laço for para imprimir todas as chaves. '''


estudante = {
    "nome": "Mateus",
    "idade": "30",
    "curso": "SI",
    "nota" : "10"
    }
for chave, valor in estudante.items():
    print(f"{chave.capitalize()}: {valor}")


