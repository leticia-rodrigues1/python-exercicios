frutas = [ "Maça", "Banana", "Kiwi", "Morango", "Uva"]

def lista_frutas(frutas):
    print("Quantidade de Frutas",len(frutas))
    print("Fruta com mais letras",max(frutas,key=len))
    print("Fruta com menos letras",min(frutas, key=len))

lista_frutas(frutas)