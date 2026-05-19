# Criar lista 
numeros = [6, 11, 14, 3, 20, 9]

# soma = 0
# % 2 == 0 par 

def somar_numeros_pares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma = soma + numero

    print(soma)

somar_numeros_pares(numeros)