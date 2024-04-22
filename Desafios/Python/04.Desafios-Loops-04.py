def fibonacci(valor):
    lista = [0, 1]
    while lista[-1] <= valor:
        lista.append(lista[-1] + lista[-2])
    return lista[:-1]

valor_limite = int(input("Digite o valor limite: "))
resultado = fibonacci(valor_limite)
print("Os números de Fibonacci até ultrapassar", valor_limite, "são:", resultado)
