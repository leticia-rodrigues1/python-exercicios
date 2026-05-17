profissoes = ["Médico", "Engenheiro", "TI", "Advogado", "Nutricionista"]
def total_profissoes(profissoes):
    print("Quantidade de profissoes", len(profissoes))
    print("Profissão com mais letras",max(profissoes,key=len))
    print("Profissão com menos letras", min(profissoes, key=len))

total_profissoes(profissoes)