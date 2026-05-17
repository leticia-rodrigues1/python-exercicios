vendas = [120,350,200,500,150]
def total_vendas(vendas):
    print("Maior Venda:", max(vendas))
    print("Menor Venda:", min(vendas))
    print("Total Vendido:", sum(vendas))
    print("Quantidade de Vendas:", len(vendas))
    print("Média de Vendas:", sum(vendas)/ len(vendas))

total_vendas(vendas)