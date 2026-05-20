# Criar a lista 
doces = [ "chocolate", "sorvete", "brigadeiro", "pudim"]
# contar quantos doces tem mais de 5 letras

def doces_com_5letras(doces):
    contador = 0
    for doce in doces:
        if len(doce) > 5:
            contador = contador + 1
    
    print(contador)

doces_com_5letras(doces)
