# Criar a lista 
estoque = [45, 12, 89, 30, 67]

# Crie uma função que mostre:
# maior quantidade em estoque
# menor quantidade em estoque
# soma total do estoque
# quantidade de itens
# média do estoque

def estoque_total(estoque):
    print("Maior", max(estoque))
    print("Menor", min(estoque))
    print("Soma", sum(estoque))
    print("Quantidade", len(estoque))
    print("Média", sum(estoque) / len(estoque))

estoque_total(estoque)