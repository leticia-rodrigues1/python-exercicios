# Criando a lista 
profissoes = ["Médico", "Engenheiro", "TI", "Advogado", "Nutricionista"]

# Def definir a função 
def total_profissoes(profissoes):
    profissoes_mais_letras = profissoes[0]
    profissoes_menos_letras = profissoes[0]

    for profissao in profissoes:
        if len(profissao) > len(profissoes_mais_letras):
            profissoes_mais_letras = profissao
        if len(profissao) < len(profissoes_menos_letras):
                profissoes_menos_letras = profissao
                
        
        print("Quantidade de profissões", len(profissoes))
        print("Profissão com mais letras", profissoes_mais_letras)
        print("Profissão com menos letras", profissoes_menos_letras)

total_profissoes(profissoes)
        

