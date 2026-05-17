# Criar a lista 
filmes = ["Avatar", "Up", "Titanic", "Interestrelar", "Matrix"]
def total_filmes(filmes):
    print("Quantidade", len(filmes))
    print("Maior",max(filmes,key=len))
    print("Menor", min(filmes,key=len))

total_filmes(filmes)