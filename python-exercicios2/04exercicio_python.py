nomes = ["Ana", "Fernanda", "João", "Carlos","Beatriz"]

def lista_nomes(nomes):
    print("Quantos nomes existem:", len(nomes))
    print("Nome com mais letras:", max(nomes, key=len))
    print("Nomecom menos letras:", min(nomes,key=len))

lista_nomes(nomes)

## key aqui significa "use o tamanho como critério"