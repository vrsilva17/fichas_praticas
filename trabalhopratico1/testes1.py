import random

class Jogador():

    def __init__(self, nome, token):
        self.nome = nome
        self.token = token
    
    def __str__(self):
        return "{}: {}".format(self.nome, self.token)

class Tabuleiro():

    def __init__(self, token):
        self.data = [ ["","",""], 
                      ["","",""], 
                      ["","",""] ]
        self.token = token
        
    def __str__(self):
        return str(self.data[0][0])
        
    def PrimeiroJogador(self):
        if random.randint(0,1) == 0:
            return 'jogador1'
        else:
            return 'jogador2'
    
    def MostrarTabuleiro(self):
        for i in range(0, 2):
            for j in range (0,2):
                if j<1:
                    print (self.token[self.data[i][j]],'| ',end="",flush=True)
                else:
                    print (self.token[self.data[i][j]],end="",flush=True)
            print(end="\n")
        print(end="\n")


# Pedir informações dos jogadores
jogador1 = input('Insira o nome do jogador 1: ')
token1 = input("Insira o token do jogador 1: ")
jogador2 = input('Insira o nome do jogador 2: ')
token2 = input("Insira o token do jogador 2: ")

while token1 == token2 :
    print('Token repetido')
    token2 = input("Insira o token do jogador 2: ")

#Imprimir Jogadores e Tokens
print(Jogador(jogador1,token1))
print(Jogador(jogador2,token2))

#Mandar os token para a class Tabuleiro
print(Tabuleiro(token1))
print(Tabuleiro(token2))

teste = Tabuleiro()
teste.MostrarTabuleiro()


