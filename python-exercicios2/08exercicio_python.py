#Criei a lista dos animais 
animais = [ "Cachorro", "Gato", "Elefante", "Rato", "Borboleta"]

# def vou definir a função
def lista_animais(animais):
    maior_letras = animais[0]
    menor_letras = animais[0]

    for animal in animais:
        if len(animal) > len(maior_letras):
            maior_letras = animal
        if len(animal) < len(menor_letras):
            menor_letras = animal
            
            print("Quantidade de animais", len(animais))
            print("Animal com mais letras", maior_letras)
            print("Animal com menos letras", menor_letras)

lista_animais(animais)
