import re
#https://docs.python.org/pt-br/3/library/re.html#module-re

def polindromo(frase):
    # Remove espaços, pontuações e caracteres especiais da frase
    limpar_frase = re.sub(r'[^a-zA-Z]', '', frase.lower())
    # Verifica se a frase limpa é igual à sua reversão
    return limpar_frase == limpar_frase[::-1]

def main():
    frase = input("Digite uma frase: ")
    
    if polindromo(frase):
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")

if __name__ == "__main__":
    main()
