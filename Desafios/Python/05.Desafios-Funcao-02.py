def palavra_mais_longa(lista_palavras):
    palavra_mais_longa = ''
    for palavra in lista_palavras:
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra
    return palavra_mais_longa

palavras = ['gato', 'cachorro', 'elefante', 'pássaro']
print("A palavra mais longa é:", palavra_mais_longa(palavras))
