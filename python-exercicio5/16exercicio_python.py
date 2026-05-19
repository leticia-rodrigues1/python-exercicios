# Criar lista 
numeros = [4, 15, 8, 22, 3, 17, 9]
def guardar_numeros(numeros):
    guardar = []
    for numero in numeros:
        if numero > 10:
            guardar.append(numero)

    print(guardar)

guardar_numeros(numeros)

