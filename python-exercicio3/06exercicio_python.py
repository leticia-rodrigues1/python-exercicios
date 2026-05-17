# Criar lista 
numeros = [12, 5, 30, 8, 17]
# def definir função
def total_numeros(numeros):
    print("Maior Número", max(numeros))
    print("Menor Número", min(numeros))
    print("Soma Total", sum(numeros))
    print("Quantidade Total", len(numeros))
    print("Média", sum(numeros) / len(numeros))

total_numeros(numeros)