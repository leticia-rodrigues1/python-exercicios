# Criar a lista
nomes = [ "mariana", "leticia", "sandra", "alfredo", 
         "walter", "maria"]

def nomes_maiusculos(nomes):
    nova_lista = []
    for nome in nomes:
        nova_lista.append(nome.upper())

    print(nova_lista)

nomes_maiusculos(nomes)