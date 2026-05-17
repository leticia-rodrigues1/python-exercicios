animais = ["Gato", "Elefante", "Rato", "Borboleta", "Cão"]

def contador_animais(animais):
    contador = 0
    for animal in animais:
        if len(animal) > 4:
            contador = contador + 1
    print("Quantidade", contador)        

contador_animais(animais)