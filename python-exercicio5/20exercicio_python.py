# Criar lista
numeros = [10, 20, 30, 40]

def metade_numeros(numeros):
    nova_lista = []

    for numero in numeros:
        numero = numero // 2
        nova_lista.append(numero)

    print(nova_lista)

metade_numeros(numeros)