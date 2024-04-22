def numeros_repetidos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    numeros_repetidos = conjunto1.intersection(conjunto2)
    return list(numeros_repetidos)

def main():
    lista1 = input("Digite os números da primeira lista separados por vírgula: ").split(',')
    lista2 = input("Digite os números da segunda lista separados por vírgula: ").split(',')
    
    lista1 = [int(num) for num in lista1]
    lista2 = [int(num) for num in lista2]
    
    numeros_repetidos_lista = numeros_repetidos(lista1, lista2)
    
    print("Números repetidos nas listas:", numeros_repetidos_lista)

if __name__ == "__main__":
    main()