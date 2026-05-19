# Criar lista 
numeros = [2, 5, 8, 10]
 
def dobrar_numeros(numeros):
    nova_lista = []
    for numero in numeros:
        numero = numero * 2
        nova_lista.append(numero)

    print(nova_lista)

dobrar_numeros(numeros)