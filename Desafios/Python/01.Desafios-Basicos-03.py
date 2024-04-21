def nomes_vogal(lista_de_nomes):
    vogais = ['a', 'e', 'i', 'o', 'u']
    nomes_com_vogal = [nome for nome in lista_de_nomes if nome.lower()[0] in vogais]
    return nomes_com_vogal

def main():
    lista_de_nomes = input("Digite uma lista de nomes separados por vírgula: ").split(',')
    nomes_vogais = nomes_vogal(lista_de_nomes)
    print("Nomes que começam com vogal:", nomes_vogais)

if __name__ == "__main__":
    main()