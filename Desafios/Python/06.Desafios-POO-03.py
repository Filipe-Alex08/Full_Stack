class RedeSocial:
    def __init__(self):
        self.amigos = []
        self.feed = []

    def adicionar_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos.append(amigo)
            print(f"{amigo} adicionado à lista de amigos.")
        else:
            print(f"{amigo} já está na sua lista de amigos.")

    def postar_mensagem(self, mensagem):
        self.feed.append(mensagem)

    def ver_feed_noticias(self):
        print("Feed de Notícias:")
        for mensagem in self.feed:
            print(mensagem)

rede_social = RedeSocial()
rede_social.adicionar_amigo("Alana")
rede_social.adicionar_amigo("Flavio")
rede_social.adicionar_amigo("Alana")

rede_social.postar_mensagem("Olá, pessoal! Estou no LinkedIn para mais uma Postagem")
rede_social.postar_mensagem("Acabei de postar mais um desafio realizado")

rede_social.ver_feed_noticias()
