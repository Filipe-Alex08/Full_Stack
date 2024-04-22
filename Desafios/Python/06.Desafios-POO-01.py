class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.desconto = 0
        self.informacao_adicional = ""

    def calcular_preco_com_desconto(self):
        preco_com_desconto = self.preco * (1 - self.desconto / 100)
        return preco_com_desconto

    def adicionar_informacao_adicional(self, informacao):
        if informacao.strip():
            self.informacao_adicional = informacao
            print("Informação adicional adicionada com sucesso!")
        else:
            print("A informação adicional não pode estar vazia.")

def obter_informacoes_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    return nome, preco

nome_produto, preco_produto = obter_informacoes_produto()

produto1 = Produto(nome_produto, preco_produto)

desconto = float(input("Digite o desconto (%): "))
produto1.desconto = desconto

informacao_adicional = input("Digite uma informação adicional para o produto (opcional): ")
produto1.adicionar_informacao_adicional(informacao_adicional)

preco_com_desconto = produto1.calcular_preco_com_desconto()
print(f"O preço com desconto é: R${preco_com_desconto:.2f}")

if produto1.informacao_adicional:
    print("Informação adicional:", produto1.informacao_adicional)
else:
    print("Não há informação adicional para este produto.")
