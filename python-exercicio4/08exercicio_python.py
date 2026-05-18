# Criar lista 
numeros = [25, 18, 7, 30, 12, 40, 5]
# def definir a função

def total_numeros(numeros):
    for numero in numeros:
        if numero < 20:
            print(numero)

total_numeros(numeros)