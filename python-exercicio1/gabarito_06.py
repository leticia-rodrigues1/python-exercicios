# Exercício 01
print("######### Exercicio 01:")

clientes = {"Lira":5000, "Alon":3000, "Julia":4500}
nova_compra = 1500
clientes["Alon"] = clientes["Alon"] + nova_compra

clientes["Marcos"] = 2000
print(clientes)

# Exercício 02
print("######### Exercicio 02:")

estoque = {"teclado":50, "mouse":120, "monitor":30}
produto = input("Digite o nome do produto:")

produto = produto.strip().lower()
if produto in estoque:
    print(f"{produto}encontrado:{estoque[produto]}unidades no estoque")
else:
    print(f"{produto}não econtrado")

# Exercício 03
print("######### Exercicio 03:")
vendas_regiao = {"Norte":15000, "Sul":22000, "Leste":18000, "Oeste":25000}

print(vendas_regiao.keys())            # keys são as chaves dos dicionários
print(vendas_regiao.values())           # values são os valores 

lista_vendas = list(vendas_regiao.values())
total_vendas = sum(lista_vendas)
qtde_vendas = len(lista_vendas)
media_vendas = total_vendas / qtde_vendas
print("Total Vendas", total_vendas)
print("Media de Vendas", media_vendas)

# Exercício 04
print("######### Exercicio 04:")
desempenho = {"Lira":[8,9,7], "Paula":[10,9,10], "Tiago":[6,7,8]}
nome = input("Digite o nome de um colaborador:")

notas = desempenho[nome]
print("Notas", notas)
print("Nome", nome) 
media_notas = sum(notas)/ len(notas)
print("Media", media_notas)

#Exercício 05
print("######### Exercicio 05:")
produtos = {"celular":1500, "camera":800, "radio":200, "fone":100}
item_removido = "radio"

produtos.pop(item_removido)
print(produtos)

celular_no_dicionario = "celular" in produtos
print(celular_no_dicionario)