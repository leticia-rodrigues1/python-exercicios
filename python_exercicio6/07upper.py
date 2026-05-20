# Criar uma nova lista 
sobremesas = [ "chocolate", "tortas", "bolos", "pudim", "sorvete"]

# Defir minha função que é o def
def maiusculas_sobremesas(sobremesas):
    lista_nova = []
    for sobremesa in sobremesas:
        lista_nova.append(sobremesa.upper())
    print(lista_nova)

maiusculas_sobremesas(sobremesas)