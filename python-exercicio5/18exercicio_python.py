# criar lista
numeros = [25, 18, 7, 30, 12, 40, 5]
def guardar_numeros(numeros):
    guardar_menor20 = []
    for numero in numeros:
        if numero < 20:
            guardar_menor20.append(numero)

    print(guardar_menor20)

guardar_numeros(numeros)
