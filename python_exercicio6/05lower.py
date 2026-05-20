# Criar a lista 
nomes = ["ANA", "CARLOS", "LETICIA", "MARIANA"]

def nomes_minusculos(nomes):
    lista_nova = []

    for nome in nomes:

        lista_nova.append(nome.lower())
    
    print(lista_nova)


nomes_minusculos(nomes)