def mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)
    
    if tamanho % 2 == 0:
        meio1 = tamanho // 2
        meio2 = meio1 - 1
        return (lista_ordenada[meio1] + lista_ordenada[meio2]) / 2
    else:
        meio = tamanho // 2
        return lista_ordenada[meio]

numeros = [10, 5, 3, 8, 7, 2, 4, 6, 9, 1]
print("Lista de números:", numeros)
print("Mediana:", mediana(numeros))
