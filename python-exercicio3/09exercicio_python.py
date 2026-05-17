# Criar a lista 
salarios = [1800, 2500, 3200, 1500, 2800]

# Maior salário
# Menor salário
# Soma total dos salários
# Quantidade Total
# Média salarial

def total_salarios(salarios):
    print("Maior", max(salarios))
    print("Menor", min(salarios))
    print("Soma", sum(salarios))
    print("Quantidade", len(salarios))
    print("Média", sum(salarios) / len(salarios))

total_salarios(salarios)


