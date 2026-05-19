# Criar a lista 
numeros = [3, 11, 8, 15, 20, 27, 6]

def numeros_pares_menor10(numeros):
    for numero in numeros:
        if numero % 2 == 0 and numero < 10:

            print(numero)

numeros_pares_menor10(numeros)