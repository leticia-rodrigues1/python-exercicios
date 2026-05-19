# Criar a lista
numeros = [3, 11, 8, 15, 20, 27, 6]

# def definir a função
def numeros_impares_menor10(numeros):
    for numero in numeros:
        if numero %2 == 1 and numero < 10:

            print(numero)

numeros_impares_menor10(numeros)