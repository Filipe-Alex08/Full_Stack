import random

def embaralhar_lista(lista):
    lista_embaralhada = lista[:]
    random.shuffle(lista_embaralhada)
    return lista_embaralhada

def main():
    lista_original = input("Digite os itens da lista separados por vírgula: ").split(',')
    lista_embaralhada = embaralhar_lista(lista_original)
    
    print("Lista Original:", lista_original)
    print("Lista Embaralhada:", lista_embaralhada)

if __name__ == "__main__":
    main()
