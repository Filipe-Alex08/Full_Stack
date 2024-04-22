def eh_sublista(sublista, lista):
    n = len(sublista)
    m = len(lista)
    
    if n > m:
        return False
    
    for i in range(m - n + 1):
        if lista[i:i+n] == sublista:
            return True
    
    return False

def main():
    lista_grande = input("Digite os itens da lista separados por vírgula: ").split(',')
    sublista = input("Digite os itens da sublista separados por vírgula: ").split(',')
    
    if eh_sublista(sublista, lista_grande):
        print("A sublista é uma sublista da lista.")
    else:
        print("A sublista não é uma sublista da lista maior.")

if __name__ == "__main__":
    main()
