# Criar a lista 
paises = ["Brasil", "Chile", "Estados Unidos", "Peru", "Japão"]

# Criar a função
def total_paises(paises):
    paises_mais_letras = paises[0]
    paises_menos_letras = paises[0]

    for pais in paises:
        if len(pais) > len(paises_mais_letras):
            paises_mais_letras = pais
        if len(pais) < len(paises_menos_letras):
            paises_menos_letras = pais
    print("Quantidade", len(paises))
    print("Maior",paises_mais_letras)
    print("Menor", paises_menos_letras)

total_paises(paises)



