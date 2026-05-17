# Exercício 01
print("######### Exercicio 01:")

vendas = [1500, 2000, 800, 3500, 1200]
total_vendas = sum(vendas)
qtde_dias = len(vendas)  # len mostra o tamanho da lista 
media_vendas = total_vendas / qtde_dias

maior_venda = max(vendas)
menor_venda = min(vendas)

print(f"Total:{total_vendas}, Média de Vendas: {media_vendas}, Maior Venda {maior_venda}, Menor venda {menor_venda}")

# Exercício 02
print("######### Exercicio 02:")

estoque =  ["monitor", "teclado", "mouse", "headset"]
estoque.append("webcam")  #append sempre adiciona um item no final da lista 
posicao_teclado = estoque.index("teclado")
estoque[posicao_teclado] = "teclado mecânico"
print(estoque)

impressora_no_estoque = "impressora" in estoque
print(impressora_no_estoque)

estoque.remove("mouse")
print(estoque)

# Exercício 03
print("######### Exercicio 03:")
fretes = [50, 80, 20, 150, 40]
fretes.sort(reverse=True)  # sort serve para colocar os itens em ordem 
print(fretes)
top_fretes = fretes[:2]
print(top_fretes)

# Exercício 04
print("######### Exercicio 04:")
rota = ["São Paulo", "Campinas", "Jundiai", "Sorocaba"]
novas_cidas = ["Itu", "Valinhos"]

rota.extend(novas_cidas)
print(rota)
posicao_sorocaba = rota.index("Sorocaba") + 1
print(f"Sorocaba é a {posicao_sorocaba} da cidade da rota")

# Exercício 05
print("######### Exercicio 05:")
precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto", "Champagne"]

vinho_escolhido = input("Digite o vinho a ser alterado:")
novo_preco = input("Novo preço:")

novo_preco = novo_preco.replace("R$", "").replace(".","").replace(",",".")
novo_preco = float(novo_preco)

posicao_vinho = vinhos.index(vinho_escolhido)
precos[posicao_vinho]= novo_preco
print(vinhos)
print(precos)