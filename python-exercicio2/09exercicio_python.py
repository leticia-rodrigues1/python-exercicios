# criar a lista
cidades = [ "Rio de Janeiro", "São Pulo", "Salvador", "BH", "Florianópolis"]

# criar a função
def lista_cidade(cidades):
    maior_letras = cidades[0]
    menor_letras = cidades[0]

    for cidade in cidades:
        if len(cidade) > len(maior_letras):
            maior_letras = cidade
        
        if len(cidade) < len(menor_letras):
            menor_letras = cidade
        
    print("Quantidade:", len(cidade))
    print("Maior número de letras", maior_letras)
    print("Menor número de letras", menor_letras)

lista_cidade(cidades)
