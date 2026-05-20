# Criar a lista
profissoes = ["médico", "bancário", "rh", "ti"]
nova_lista = []
def nomes_profissoes(profissoes):
    for profissao in profissoes:
        nova_lista.append(profissao.upper())
    
    print(nova_lista)

nomes_profissoes(profissoes)