# Criar lista 
nomes = ["Ana", "Fernanda", "João","Carlos","Beatriz","Mariana"]

# Def criar função
def contar_nomes(nomes):
    contador = 0

    for nome in nomes:
        if len(nome) > 5:
            contador = contador + 1
    print("Quantidade", contador)

contar_nomes(nomes)

