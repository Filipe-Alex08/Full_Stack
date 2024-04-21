def remover_repetidos():
    numeros = input("Digite uma lista de números separados por espaço: ")
    numeros_lista = numeros.split()
    sem_repeticao = sorted(list(set(numeros_lista)))
    return sem_repeticao

lista_sem_repeticao = remover_repetidos()
print("Lista sem números repetidos em ordem crescente:", lista_sem_repeticao)
