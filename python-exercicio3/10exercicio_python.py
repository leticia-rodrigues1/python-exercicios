# Criar a lista 
salarios = [1800, 2500, 3200, 1500, 2800]

# Maior salário
# Menor salário
# Soma total dos salários
# Quantidade Total
# Média salarial
salarios = [1800, 2500, 3200, 1500, 2800]

def total_salarios(salarios):
    maior_salario = salarios[0]
    menor_salario = salarios[0]
    soma = 0

    for salario in salarios:
        if salario > maior_salario:
            maior_salario = salario

        if salario < menor_salario:
            menor_salario = salario

        soma = soma + salario

    media = soma / len(salarios)

    print("Maior:", maior_salario)
    print("Menor:", menor_salario)
    print("Quantidade:", len(salarios))
    print("Média:", media)
    print("Soma:", soma)

total_salarios(salarios)