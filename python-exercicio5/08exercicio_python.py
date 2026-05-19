# Criar lista 
numeros = [5, 12, 9, 20, 7, 18, 11]

# Criar definição def
def conta_impares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 1:
            contador = contador + 1

    print(contador)

conta_impares(numeros)