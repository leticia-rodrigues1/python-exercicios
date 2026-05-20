# Criar lista 
nomes = ["ana", "carlos", "beatriz", "joao"]
# Quantos nomes tem mais de 5 letras?
# contador = 0

def nomes_grandes(nomes):
    contador = 0
    for nome in nomes:
        if len(nome) > 5:
            contador = contador + 1
      

    print(contador)

nomes_grandes(nomes)