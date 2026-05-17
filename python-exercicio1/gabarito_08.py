# Exercício 01
print("######### Exercicio 01:")

produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", " caixa de som bluetooth " ]

def padronizar_texto(texto): # def é definir uma função, usado para criar uma função
    texto = texto.strip() #strip tira os espaços vazios
    texto = texto.title() #title vai colocar as primeiras letras em maiúsculas
    return texto

# 3 maneiras de fazer a lista
 # 1 opção
produtos_padronizados = []
for produto in produtos_baguncados:
    produto_padronizado = padronizar_texto(produto)
    produtos_padronizados.append(produto_padronizado)
    print(produtos_padronizados)

# 2 opção 
produtos_padronizados2 = [padronizar_texto(produto)for produto in produtos_baguncados]
print(produtos_padronizados2)

# 3 opção
produtos_padronizados3 = list(map(padronizar_texto, produtos_baguncados))
print(produtos_padronizados3)

# Exercício 02
print("######### Exercicio 02:")

def calcular_iss(valor):
    if valor > 5000:
        taxa = 0.05
    else:
        taxa = 0.03
        imposto = valor * taxa
        return imposto
    
print(calcular_iss(8000))
print(calcular_iss(2000))

 #Exercício 03
print("######### Exercicio 03:")

def analisar_magem(faturamento,custo):
    lucro = faturamento - custo
    margem = lucro / faturamento
    if margem >= 0.3:
        return "Margem Saudável"
    else:
        return "Margem Baixa"

print(analisar_magem(10000,6000))

# Exercício 04
print("######### Exercicio 04:")

def quem_bateu_meta(vendas_vendedores:dict, meta:float):
    for vendedor in vendas_vendedores:
        if vendas_vendedores[vendedor] >= meta:
            print(f"Vendedor{vendedor}bateu a meta!")


dic_vendedores = { "João": 12000, "Maria": 9500, "Ricardo": 10000, "Fernanda": 15200, "Paulo": 5000 }
meta = 10000
quem_bateu_meta(dic_vendedores,meta)

# Exercício 05
print("######### Exercicio 05:")

def converter_para_real(valor_em_dolares, cotacao_dolar):
    valor_em_real = valor_em_dolares * cotacao_dolar
    return valor_em_real

def processar_lista_precos(lista_precos_dolar, cotacao_dolar):
    for item in lista_precos_dolar:
        valor_reais = converter_para_real(item,cotacao_dolar)
    print(f"O item custa U${item} e em reias: R${valor_reais}")

precos_usd = [100, 50, 250]
cotacao_dolar = 5.20

processar_lista_precos(precos_usd,cotacao_dolar)