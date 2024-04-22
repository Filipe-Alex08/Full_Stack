def remover_duplicados(lista):
    lista_sem_duplicados = []
    for item in lista:
        if item not in lista_sem_duplicados:
            lista_sem_duplicados.append(item)
    return lista_sem_duplicados

def main():
    lista = input("Digite os itens da lista separados por vírgula: ").split(',')
    
    lista_sem_duplicados = remover_duplicados(lista)
    
    print("Lista sem itens duplicados:", lista_sem_duplicados)

if __name__ == "__main__":
    main()
