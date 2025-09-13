funcionarios = {
    "Carmem": 3565.0,
    "Breno": 2353.0,
    "Karlah": 12321.0,
    "Diego": 6709.0,
    "Eduardo": 3333.0
}

for funcionario, salario in funcionarios.items():
    novo_salario = salario * 1.10
    print(f"{funcionario} - novo salário: R$ {novo_salario:.2f}")