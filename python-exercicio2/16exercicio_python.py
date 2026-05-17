# Criar lista
paises = ["Brasil", "Chile", "Estados Unidos", "Peru", "Japão"]

# def definir a função 
def total_paises(paises):
    print("Quantidade", len(paises))
    print("Maior", max(paises,key=len))
    print("Menor", min(paises,key=len))

total_paises(paises)