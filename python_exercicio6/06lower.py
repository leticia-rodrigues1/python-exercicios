# Criar a lista 
nomes = [ "MARIANA", "CELINA", "CLARA", "CECILIA", "LETICIA"]
# Definir a função def 
def nomes_minuculos(nomes):
    nova_lista = []
    for nome in nomes:
        nova_lista.append(nome.lower())
    print(nova_lista)

nomes_minuculos(nomes)