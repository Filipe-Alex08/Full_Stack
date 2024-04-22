def elementos_comuns(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    elementos_comuns = conjunto1.intersection(conjunto2)
    return list(elementos_comuns)

def main():
    lista1 = input("Digite a primeira lista separados por vírgula: ").split(',')
    lista2 = input("Digite a segunda lista separados por vírgula: ").split(',')
    
    elementos = elementos_comuns(lista1, lista2)
    
    print("Elementos comuns às duas listas:", elementos)

if __name__ == "__main__":
    main()