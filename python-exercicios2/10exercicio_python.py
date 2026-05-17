cidades = [ "Rio de Janeiro", "São Pulo", "Salvador", "BH", "Florianópolis"]
def lista_cidades(cidades):
    print("Quantidade de cidades:", len(cidades))
    print("Maior número de letras:",max(cidades,key=len))
    print("Menor número de ltras", min(cidades, key=len))

lista_cidades(cidades)