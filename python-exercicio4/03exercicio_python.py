# Criar a lista
estoques = [45, 12, 89, 30, 67]
# Definir a função
def total_estoque(estoques):
    maior_estoque = estoques [0]
    menor_estoque = estoques [0]
    soma = 0 
    for estoque in estoques:
        if estoque > maior_estoque:
            maior_estoque = estoque
        if estoque > menor_estoque:
            menor_estoque = estoque
            soma = soma + estoque
            print("Maior", maior_estoque)
            print("Menor", menor_estoque)    
            print("Quantidade", len(estoques))
            print("Soma", soma)
            print("Média", soma / len(estoques))

total_estoque(estoques)