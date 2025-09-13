produtos = {
    "Arroz": 9.34,
    "Feijão": 6.49,
    "Macarrão": 7.05,
    "Óleo": 7.80,
    "Açúcar": 5.50
}

total = 0
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")
    total += preco

print("Valor total da compra:", total)