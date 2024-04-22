def soma_digitos(numero):
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    return soma

numero = int(input("Digite um número inteiro: "))
resultado = soma_digitos(numero)
print("A soma dos dígitos de", numero, "é:", resultado)
