# Crie uma função que mostre:

# maior temperatura
# menor temperatura
# soma total das temperaturas
# quantidade de temperaturas
# média

# Lista 
temperaturas = [28, 35, 22, 40, 31]
def total_temperaturas(temperaturas):

    maior_temperatura = temperaturas [0]
    menor_temperatura = temperaturas [0]
    soma = 0

    for temperatura in temperaturas:
        if temperatura > maior_temperatura:
            maior_temperatura = temperatura

        if temperatura < menor_temperatura:
            menor_temperatura = temperatura

        soma = soma + temperatura
        
    print("Maior", maior_temperatura)
    print("Menor", menor_temperatura)
    print("Soma", soma)
    print("Quantidade", len(temperaturas))
    print("Média", soma /len(temperaturas))

total_temperaturas(temperaturas)




