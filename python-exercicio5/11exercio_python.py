# numero impar % 2 == 1
# soma = 0
# criar a lista
numeros = [5, 12, 9, 20, 7, 18, 11]

def somar_impares(numeros):
    soma = 0
    for numero in numeros:
        if numero % 2 == 1:
            soma = soma + numero
    
    print(soma)

somar_impares(numeros)