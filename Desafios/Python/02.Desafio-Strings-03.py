def mensagem_criptografada(mensagens):
    frases = ""
    for caractere in mensagens:
        if caractere.isalpha():  # Verifica se o caractere é uma letra
            if caractere.islower():  # Verifica se o caractere é minúsculo
                caractere_criptografado = chr((ord(caractere) - ord('a') + 3) % 26 + ord('a'))
            else:  # O caractere é maiúsculo
                caractere_criptografado = chr((ord(caractere) - ord('A') + 3) % 26 + ord('A'))
        else:  # Mantém caracteres não alfabéticos
            caractere_criptografado = caractere
        frases += caractere_criptografado
    return frases

def main():
    mensagens = input("Digite a mensagem a ser criptografada: ")
    frases = mensagem_criptografada(mensagens)
    print("Mensagem criptografada:", frases)

if __name__ == "__main__":
    main()

"""
Me apoiei a uma atividade que tinha feito no curso da Infinity, porém ele não chegava a dar o print da função. 
O programa em si consiste em solicitar ao usuário que digite uma mensagem e, em seguida, criptografa a mensagem usando a técnica de substituição de letras, onde cada letra é substituída por uma letra que esteja três posições à frente no alfabeto. 
O programa lida com letras maiúsculas e minúsculas, mantendo caracteres não alfabéticos intactos.
"""