# Criar lista 
numeros = [4, 12, 7, 18, 9, 21, 30]

def numeros_pares(numeros):
    for numero in numeros:
        if numero % 2 == 0 and numero > 10:
            print(numero)

numeros_pares(numeros)