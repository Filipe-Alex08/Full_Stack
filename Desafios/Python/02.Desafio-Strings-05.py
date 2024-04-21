def ordenar_palavras(frase):
    palavras = frase.split()
    palavras_ordenadas = sorted(palavras)
    return ' '.join(palavras_ordenadas)

def main():
    frase = input("Digite uma frase: ")
    nova_frase = ordenar_palavras(frase)
    print("Nova frase com as palavras em ordem alfabética:", nova_frase)

if __name__ == "__main__":
    main()
