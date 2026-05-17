# Exercício 01
# primeiro cria as variáveis 
faturamento_inicial = 50000
percentual_bonus = 0.1    #0.1 = 10%
bonus_total = faturamento_inicial * percentual_bonus
faturamento_liquido = faturamento_inicial - bonus_total
print(faturamento_liquido)
print(bonus_total)

# Exercício 02
estoque = 250
vendas = 78
reposicao = 100
estoque = estoque - vendas + reposicao
print(estoque)

# Exercício 03
caixas = 1250
capacidade_caminhao = 12

caminhoes_completos = caixas // capacidade_caminhao
# % resto da divisão 
# // divisão inteira
print(caminhoes_completos)

caixas_restantes = caixas % capacidade_caminhao
print(caixas_restantes)

# Exercício 4
faturamento = 15000
custos_fixos = 5000
percentual_imposto = 0.15 # 0.15 = 15%

imposto = faturamento * percentual_imposto
lucro = faturamento - custos_fixos - imposto
margem = lucro / faturamento
print("imposto", imposto)
print("lucro liquido", lucro)
print("margem", margem)
print("faturamento", faturamento)

meta_atingida = margem > 0.3 #30%
print(meta_atingida)

# Exercício 05
duracao = 40
anos = 40 // 12
meses_sobram = 40 % 12
print("duração do contrato é de", anos, "anos e", meses_sobram, "meses")