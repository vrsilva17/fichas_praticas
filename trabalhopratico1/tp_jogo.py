import csv
from tp_jogador import Jogador

class Jogo():

    def __init__(self):
        self.lista_jogadores = []
        self.lista_token = []
        self.pontuacao = 0
        self.jogos_jogados = 0

    def __str__(self):
        return "Nomes dos jogadores em uso: {}  \n  Tokens em utilização: {}".format(self.lista_jogadores, self.lista_token)

    def inserir_jogador(self):
        nome = input("Indique o seu nome: ")
        self.lista_jogadores.append(nome)
    
    def validar_token(self, token):
        if token in self.lista_token:
            return True
        else:
            return False  
    
    def inserir_token(self, token):
        if self.validar_token(token) == True:
            print("Token já em uso")
        else:
            self.lista_token.append(token)
            print("Token Inserido com sucesso")

if __name__ == "__main__":

    p1 = Jogo()
    p1.inserir_jogador()
    token = input("Escolha o seu token: ")
    p1.inserir_token(token)
    p1.inserir_jogador()
    token = input("Escolha outro token: ")
    p1.inserir_token(token)
    p1.inserir_jogador()
    token = input("Escolha outro token: ")
    p1.inserir_token(token)

    print(p1)
