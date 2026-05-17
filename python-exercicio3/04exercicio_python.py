# Criar a lista
idades = [18, 25, 16, 32, 14, 40, 19]

# def criar a função

def contador_idades(idades):
    contador = 0
    for idade in idades:
          if idade >= 18:
              contador = contador + 1
    print(contador)

contador_idades(idades)