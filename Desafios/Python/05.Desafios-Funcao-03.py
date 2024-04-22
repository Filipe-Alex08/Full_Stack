def numeros_pares(lista_numeros):
    return [num for num in lista_numeros if num % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números pares:", numeros_pares(numeros))
