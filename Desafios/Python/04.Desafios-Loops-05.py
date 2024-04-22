def calcular_media(lista):
    total = 0
    for elemento in lista:
        total += elemento
    media = total / len(lista)
    return media

lista_numeros = [10, 20, 30, 40, 50]
media = calcular_media(lista_numeros)
print("A média dos números na lista é:", media)
