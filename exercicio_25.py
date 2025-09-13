
''' 25. Crie uma lista de 10 números. Use um laço for para imprimir a tabuada de cada 
número. '''

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

tabuada = []

for t in a:
    for multiplicador in range(0, 9):
        resultado = t * multiplicador
        print(f"{t} x {multiplicador} = {resultado}")
    

