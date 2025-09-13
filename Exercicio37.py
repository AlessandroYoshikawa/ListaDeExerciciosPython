cursos = {
    "Linguagem de Programação": "Java",
    "Algorítimo": "C++",
    "Sistemas de Informação": "Python",
    "Programação Web": "JavaScript"
}

encontrado = False

for linguagem in cursos.values():
    if linguagem == "Python":
        encontrado = True
        break

if encontrado:
    print("Tem Python em algum curso")
else:
    print("Não tem Python em nenhum curso")