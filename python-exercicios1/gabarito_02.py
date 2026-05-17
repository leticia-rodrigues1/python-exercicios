# Exercício 01
print("######### Exercicio 01:")
faturamento = 45000
custo = 23500
lucro = faturamento - custo
margem = lucro / faturamento
print(f"Lucro: R${lucro:,.2f}, Margem:{margem:.0%}")  # f com os { } trasnforma em variáveis

# Exercício 02
print("######### Exercicio 02:")
# Remover os espaços extras no início e fim das duas variáveis. 
# Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo.
# Deixar o e mail todo em letras minúsculas.

nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "

nome = nome.strip()             # strip tira os valores/espaços vazios 
nome = nome.title()        # title coloca a primeira letra em maiúscula
print(nome)

emial = email.strip()   # strip remove os espaços vazios 
email = email.lower()   # lower coloca tudo em letra minúscula 
print(email)

# Exercício 03
print("######### Exercicio 03:")
email = "andre_silva@empresa.com.br" 
novo_dominio = "@grupocorp.com"
posicao_arroba = email.find("@")   # find mostra o número da posição do texto  
print(posicao_arroba)

email = email[:11] + novo_dominio
print(email)

email = email.replace("@empresa.com.br", "@grupocorp.com")
print(email)


# Exercício 04
print("######### Exercicio 04:")
email = "beatriz.oliveira@grupocorp.com"
posicao_arroba = email.find("@")

print(posicao_arroba)

username = email[:posicao_arroba]
print(username)

# Exercício 05
print("######### Exercicio 05:")
# Encontrar a posição do primeiro espaço
# Fatiar o texto para pegar apenas o primeiro nome
# Formatar o nome com a primeira letra maiúscula 
# Exibir a mensagem "Olá,[Primeiro Nome], seja bem-vindo ao nosso clube!"

mensagem = "Olá,[Primeiro Nome], seja bem-vindo ao nosso clube!"
nome_usuário = "lucas ferreira souza"
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco].capitalize()
print(primeiro_nome)

mensagem = mensagem.replace("[Primeiro Nome]",primeiro_nome)
print(mensagem)