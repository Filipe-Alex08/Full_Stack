import random

class Baralho:
    def __init__(self):
        self.cartas = []
        self.__iniciar_baralho()

    def __iniciar_baralho(self):
        naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
        valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
        self.cartas = [(valor, naipe) for naipe in naipes for valor in valores]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir_mao(self, num_cartas=5):
        if num_cartas > len(self.cartas):
            print("Não há cartas suficientes para distribuir uma mão.")
            return []
        mao = [self.cartas.pop() for _ in range(num_cartas)]
        return mao

# Exemplo de uso
baralho = Baralho()
baralho.embaralhar()
mao_jogador1 = baralho.distribuir_mao()
mao_jogador2 = baralho.distribuir_mao()

print("Mão do Jogador 1:", mao_jogador1)
print("Mão do Jogador 2:", mao_jogador2)