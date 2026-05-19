# Criar lista
numeros = [2, 15, 8, 21, 14, 33, 40]

# Crie uma função que conte quantos números são pares.
def contar_pares(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 0:
            contador = contador + 1
            
    print(contador)

contar_pares(numeros)