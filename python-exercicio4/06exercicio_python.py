# Lista 
sapatos = [ 10, 50, 10, 30,]

def total_sapatos(sapatos):
    maior_sapato = sapatos [0]
    menor_sapato = sapatos [0]
    soma = 0

    for sapato in sapatos:
        if sapato > maior_sapato:
            maior_sapato = sapato
        if sapato < menor_sapato:
            menor_sapato = sapato
        
        soma = soma + sapato

    print("Maior", maior_sapato)
    print("Menor", menor_sapato)
    print("Quantidade", len(sapatos))
    print("Média", soma / len(sapatos))
    print("Soma", soma)

total_sapatos(sapatos)