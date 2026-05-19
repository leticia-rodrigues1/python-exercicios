# Criar lista 
numeros = [4, 15, 8, 22, 3, 17, 9]
def guardar_numeros_menores10(numeros):
    menores10 = []
    for numero in numeros:
        if numero < 10:
            menores10.append(numero)
    
    print(menores10)

guardar_numeros_menores10(numeros)