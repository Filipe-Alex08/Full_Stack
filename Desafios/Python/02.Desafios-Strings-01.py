def ocorrencias(frase, palavra):
    # Converte a frase e a palavra para minúsculas para tornar a comparação sem diferenciação de maiúsculas/minúsculas
    frase_lower = frase.lower()
    palavra_lower = palavra.lower()
    
    # Divide a frase em palavras
    palavras = frase_lower.split()
    
    # Inicializa o contador de ocorrências da palavra
    contar = 0
    
    # Itera sobre as palavras na frase
    for w in palavras:
        # Se a palavra na frase for igual à palavra especificada, incrementa o contador
        if w == palavra_lower:
            contar += 1
    
    return contar

def main():
    frase = input("Digite uma frase: ")
    palavra = input("Digite a palavra que deseja contar: ")
    
    contar = ocorrencias(frase, palavra)
    print(f"A palavra '{palavra}' aparece na frase {contar} vezes.")

if __name__ == "__main__":
    main()