alunos = {
    "Alessandro": [9.1, 9.3],
    "Rafael": [8.0, 9.5],
    "João Vitor": [9.3, 8.1],
    "Paulo Sérgio": [7.3, 8.6],
    "Beatriz": [8.0, 8.5]
}

for aluno, notas in alunos.items():
    media = sum(notas) / len(notas)
    print(f"{aluno} tem média {media:.2f}")