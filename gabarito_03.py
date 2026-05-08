# Exercício 01
print("######### Exercicio 01:")

faturamento = input("Digite o faturamento:")
faturamento = faturamento.replace("R$", "").replace(".", "").replace(",",".")
faturamento_numerico = float(faturamento)
perc_imposto = 0.15
imposto = faturamento_numerico * perc_imposto
print(f"Imposto pago: R${imposto:,.2f}")


# Exercício 02
print("######### Exercicio 02:")
mensagem = "Cadastro concluído:[Primeiro Nome]. E-mail de acesso: [E-mail padronizado]"

nome = input("Digite o nome completo do colaborador:")
email = input("Digite o email do colaborador:")

nome = nome.strip()
email = email.strip().lower()

posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco].capitalize() 

mensagem = mensagem.replace("[Primeiro Nome]", primeiro_nome).replace("[E-mail padronizado]", email)
print(mensagem)

# Exercício 3
print("######### Exercicio 03:")
fat_lojaA = input("Faturamento da loja A:")
fat_lojaB = input("Faturamento da loja B:")

fat_lojaA = fat_lojaA.replace("R$", "").replace(".", "").replace(",",".")
fat_lojaA = float(fat_lojaA)

fat_lojaB = fat_lojaA.replace("R$", "").replace(".", "").replace(",",".")
fat_lojaB = float(fat_lojaB)

total_fat = fat_lojaA + fat_lojaB
media_fat = total_fat / 2

print(f"Faturamento Total: R${total_fat:,.2f}, Média de Faturamento: R${media_fat:,.2f}")
