# Criaer lista
nomes = ["ana", "carlos", "beatriz", "joao"]

def arrumar_nomes(nomes):
    lista_nomes_arrumados = []

    for nome in nomes:

        lista_nomes_arrumados.append(nome.capitalize())

    print(lista_nomes_arrumados)

arrumar_nomes(nomes)