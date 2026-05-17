# Criar lista
numeros = [10, 7, 22, 15, 8, 3, 14]

# def criar função
def contar_pares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador = contador + 1
    print(contador)

contar_pares(numeros)
