def inverter_palavras(frase):
    palavras = frase.split()
    palavras_invertidas = [palavra[::-1] for palavra in palavras]
    return ' '.join(palavras_invertidas)

frase = "Hello World, como vai?"
print("Frase original:", frase)
print("Frase com palavras invertidas:", inverter_palavras(frase))
