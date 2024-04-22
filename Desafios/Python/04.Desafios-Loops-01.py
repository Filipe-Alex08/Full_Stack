def encontrar_maior(lista):
    if not lista:
        return None
    
    maior = lista[0]
    for elemento in lista:
        if elemento > maior:
            maior = elemento
    return maior

def main():
    lista = input("Digite os itens da lista separados por vírgula: ").split(',')
    lista = [int(numero.strip()) for numero in lista]
    
    maior = encontrar_maior(lista)
    if maior is not None:
        print("O maior elemento da lista é:", maior)
    else:
        print("A lista está vazia.")

if __name__ == "__main__":
    main()
