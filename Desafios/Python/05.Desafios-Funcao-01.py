def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores.append(i)
    return divisores

num = 12
print("Os divisores de", num, "são:", encontrar_divisores(num))
