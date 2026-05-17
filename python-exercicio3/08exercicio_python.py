# Criar lista 
numeros = [12, 5, 30, 8, 17]

# def definir função
def total_numeros(numeros):
    maior_numero = numeros [0]
    menor_numero = numeros [0]
    soma = 0
    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero

        if numero < menor_numero:
            menor_numero = numero
    
        media = soma/ len(numeros)
        soma = soma + numero

    print("Maior", maior_numero)
    print("Menor", menor_numero)
    print("Quantidade", len(numeros))
    print("Média", media)
    print("Soma", soma)

total_numeros(numeros)
    