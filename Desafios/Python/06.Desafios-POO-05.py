class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_com_desconto(self, desconto):
        return self.preco * (1 - desconto)


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def calcular_total(self):
        return sum(produto.preco for produto in self.produtos)


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = CarrinhoDeCompras()

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.adicionar_produto(produto)

    def finalizar_compra(self):
        total = self.carrinho.calcular_total()
        print(f"{self.nome}, o total da sua compra é R${total:.2f}.")
        return total

produto1 = Produto("Camiseta", 50)
produto2 = Produto("Calça", 100)
produto3 = Produto("Tênis", 200)

cliente = Cliente("Filipe")
cliente.adicionar_ao_carrinho(produto1)
cliente.adicionar_ao_carrinho(produto2)
cliente.adicionar_ao_carrinho(produto3)

total_compra = cliente.finalizar_compra()
