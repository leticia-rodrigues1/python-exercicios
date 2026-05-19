# Criar lista 
numeros = [4, 7, 10, 15, 8, 3]

# def
# vou usar numero % 2 == 0
# vou usar sum para somar os números pares

def numeros_pares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma = soma + numero
    print(soma)


numeros_pares(numeros)