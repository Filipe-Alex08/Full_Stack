def is_primos(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def filtro_primos(numeros):
    numeros_unicos = set(numeros)
    numeros_primos = [num for num in numeros_unicos if is_primos(num)]
    return numeros_primos

def main():
    numeros_str = input("Digite uma lista de números separados por vírgula: ")
    numeros = [int(num.strip()) for num in numeros_str.split(',')]
    numeros_primos = filtro_primos(numeros)
    print("Números primos:", numeros_primos)

if __name__ == "__main__":
    main()
