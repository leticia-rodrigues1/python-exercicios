

# Crie uma função que mostre:
# maior quantidade em estoque
# menor quantidade em estoque
# soma total do estoque
# quantidade de itens
# média do estoque

estoques = [45, 12, 89, 30, 67]

def total_estoque(estoques):
    soma = 0
    valor_maior = estoques[0]
    valor_menor = estoques[0]

    for estoque in estoques:
        if estoque > valor_maior:
            valor_maior = estoque

        if estoque < valor_menor:
            valor_menor = estoque

        soma = soma + estoque

    print("Maior:", valor_maior)
    print("Menor:", valor_menor)
    print("Quantidade:", len(estoques))
    print("Soma:", soma)
    print("Média:", soma / len(estoques))

total_estoque(estoques)