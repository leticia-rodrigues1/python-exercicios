# Exercício 01
print("######### Exercicio 01:")

valor = input("Digite o valor que você vai querer investir:")
valor = valor.replace("R$","").replace(".", "").replace(",",".")
valor = float(valor)

if valor < 1000:
   print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor <= 5000:
   print("Perfil moderado: Sugerimos Fundos Imobiliários")
else:
   print("Perfil arrojado: Sugerimos Ações")

    # Exercício 02
print("######### Exercicio 02:")

admins = ["ana@empresa.com", "guilherme@empresa.com","felipe@empresa.com"]

email = input("Digite seu email:")
email = email.strip().lower()

if email in admins:
    print("Acesso liberado!Bem-vindo ao painel de controle")
else:
   print("Acesso negado. Você não tem permissão de administrador")

    # Exercício 03
print("######### Exercicio 03:")
valor_carrinho = 5000

if valor_carrinho < 200:
    perc_desconto = 0
elif valor_carrinho < 500:
    perc_desconto = 0.1
else: 
    perc_desconto = 0.15

desconto = valor_carrinho * perc_desconto
valor_final = valor_carrinho - desconto 
print(f"Desconto:R${desconto:,.2f}.Valor Total:{valor_final:,.2f}")

# Exercício 04
print("######### Exercicio 04:")
meta = 1000
vendas_vendedor = 1200

meta_loja = 5000
vendas_loja = 6500

if vendas_loja >= meta_loja and vendas_vendedor >= meta:
    bonus = 0.2 * vendas_vendedor
else:
    bonus = 0

print(f"Seu bônus este mês é de: R${bonus:,.2f}")

# Exercício 05
print("######### Exercicio 05:")
assunto = "Problemas com pagamento"

assunto = assunto.lower()  # lower é colocar tudo em letra em minúculas

if "pagamento" in assunto or "boleto" in assunto:
    print("Encaminhado para o setor financeiro")
elif "entrega" in assunto or "atraso" in assunto:
    print("Encaminhado para logística")
else:
    print("Encaminhado para o suporte geral")