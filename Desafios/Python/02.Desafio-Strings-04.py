def contar_palavras(lista_palavras):
    contagem = {}
    for palavra in lista_palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

def main():
    lista_palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
    contagem_palavras = contar_palavras(lista_palavras)
    print("Contagem de palavras:", contagem_palavras)

if __name__ == "__main__":
    main()