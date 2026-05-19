# criar a lista
# def definir funçaõ
# usar numero 2 % == 1 ímpar 
# usar o append para adicionar item na lista

numeros = [3, 8, 11, 20, 7, 14, 9]
def guardar_ímpares(numeros):
    impares = []
    
    for numero in numeros:
        if numero % 2 == 1:
            impares.append(numero)

    print(impares)

guardar_ímpares(numeros)