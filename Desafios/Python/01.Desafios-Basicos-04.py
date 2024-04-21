def encontrar_texto_longa(lista_de_textos):
    texto_longo = max(lista_de_textos, key=len)
    return texto_longo

def main():
    lista_de_textos = input("Digite uma lista de texto separadas por vírgula: ").split(',')
    texto_longo = encontrar_texto_longa(lista_de_textos)
    print("O texto mais longa é:", texto_longo)

if __name__ == "__main__":
    main()
