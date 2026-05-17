# Mostrar:
# A quantidade de filmes
# Filme com MAIS letras
# Filem com MENOS letras

# Criar a lista 
filmes = ["Avatar", "Up", "Titanic", "Interestrelar", "Matrix"]

# Criar a def criando uma função 
def total_filmes(filmes):
    filmes_mais_letras = filmes[0]
    filmes_menos_letras = filmes[0]
    
    for filme in filmes:
        if len(filme) > len(filmes_mais_letras):
            filmes_mais_letras = filme
            if len(filme) < len(filmes_menos_letras):
                filmes_menos_letras = filme 
        
        
    print("Quantidade de filme", len(filmes))
    print("Filmes com mais letras", max(filmes,key=len))
    print("Filmes com mais letras", min(filmes,key=len))

total_filmes(filmes)



