
# Mostre:
# quantidade de frutas
# fruta com MAIS letras 
# fruta com MENOS letras 

frutas = [ "Maça", "Banana", "Kiwi", "Morango", "Uva"]
def lista_frutas(frutas):
    maior_nome_frutas = frutas[0]
    menor_nome_frutas = frutas [0]

    for fruta in frutas:
        if len(fruta) > len(maior_nome_frutas):
            maior_nome_frutas = fruta 
        if len(fruta) < len(menor_nome_frutas):
            menor_nome_frutas = fruta
            print("Quantidade de frutas", len(frutas))
            print("Frutas com mais letras", maior_nome_frutas)
            print("Frutas com menos letras", menor_nome_frutas)

lista_frutas(frutas)