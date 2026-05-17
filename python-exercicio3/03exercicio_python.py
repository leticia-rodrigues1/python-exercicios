produtos = ["Notebook", "Mouse", "Teclado", "HD", "Monitor", "Cabo"]

def contador_produtos(produtos):
    contador = 0
    for produto in produtos:
        if len(produto) > 6:
            contador = contador + 1
    print("Quantidade", contador) 

contador_produtos(produtos)  