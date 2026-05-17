# criar lista
numeros = [12, 5, 30, 8, 17]

# def definir função 
def total_numeros(numeros):
    maior_numero = numeros[0]
    menor_numero = numeros[0]
    soma = 0
    for numero in numeros:
        if numero > maior_numero:
            maior_numero = numero

        if numero < menor_numero:
            menor_numero = numero
            
        soma = soma + numero
        media = soma / len(numeros)

    print("Maior", maior_numero)
    print("Menor", menor_numero)
    print("Soma", soma)
    print("Quantidade", len(numeros))
    print('Média', media)

total_numeros(numeros)