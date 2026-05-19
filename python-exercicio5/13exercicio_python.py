# números impares numero % 2 == 1
# soma = 0
# criar lista
numeros = [8, 5, 13, 22, 7, 10]

def somar_numeros_impares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 1:
            soma = soma + numero
    print(soma)

somar_numeros_impares(numeros)