def obter_lista_de_numeros():
    numeros = input("Digite uma sequência de números separados por vírgula: ")
    numeros_lista = numeros.split(',')
    numeros_lista = [int(numero.strip()) for numero in numeros_lista]
    numeros_lista.sort()
    return numeros_lista

lista_de_numeros = obter_lista_de_numeros()
print("Lista de números:", lista_de_numeros)
