# Colocar nomes em maiúsculo
# Criar a lista:
nomes = ["ana", "carlos", "beatriz", "joao"]

def nomes_maiusculo(nomes):
    nova_lista = []

    for nome in nomes:
        nova_lista.append(nome.upper())
        
    print(nova_lista)

nomes_maiusculo(nomes)