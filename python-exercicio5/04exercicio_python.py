# Criar lista
numeros = [3, 11, 8, 15, 20, 27, 6]

def numeros_impares(numeros):
    for numero in numeros:

        if numero % 2 == 1 and numero >10:
            
            print(numero)

numeros_impares(numeros)