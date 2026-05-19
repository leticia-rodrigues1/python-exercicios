# Guardar números pares em uma nova lista 
# Criar a lista 
# Números pares numero % 2 == 0

numeros = [3, 8, 11, 20, 7, 14, 9]
def guardar_pares(numeros):
    pares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)

    print(pares)

guardar_pares(numeros)