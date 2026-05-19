# Criar lista 
numeros = [5, 13, 8, 21, 4, 17, 30]

# Contar quantos números impares e maiores que 10
# Vou usa % 2 == 1 , and e contador

def numeros_impares_maiores10(numeros):
    contador = 0
    for numero in numeros:
        if numero % 2 == 1 and numero > 10:
            contador = contador + 1

    print (contador)

numeros_impares_maiores10(numeros)