# Criar a lista 
cidades = ["rio", "salvador", "recife", "curitiba"]
lista_nova = []

def nomes_cidades(cidades):
    for cidade in cidades:
        lista_nova.append(cidade.upper())
    
    print(lista_nova)

nomes_cidades(cidades)