##Variaveis globais
jogador_valido = False

##Class Jogador
class jogador():
    
    def __init__(self):
        self.nome = ""
        self.token = ""

    def validar_jogador(self):
        while jogador1.token == jogador2.token:
            print("Token do Jogador 2 repetido!")
            jogador2.token = input("[Jogador 2] Introduza um novo Token: ")
        return self.token
        
##Class Tabuleiro
class tabuleiro():
    
    def __init__(self):

        self.tabuleiro = [ [None, None, None], 
                           [None, None, None], 
                           [None, None, None] ]

    def __str__(self):
        print( ' |    A   |    B    |     C   |')
        print( '-----------------------------')
        print( '1|  {}    |   {}    |   {}    |'.format(self.tabuleiro[0][0], self.tabuleiro[0][1], self.tabuleiro[0][2]))
        print( '-----------------------------')
        print( '2|  {}    |   {}    |   {}    |'.format(self.tabuleiro[1][0], self.tabuleiro[1][1], self.tabuleiro[1][2]))
        print( '-----------------------------')
        print( '3|  {}    |   {}    |   {}    |'.format(self.tabuleiro[2][0], self.tabuleiro[2][1], self.tabuleiro[2][2]))
        print( '-----------------------------')
    
    #def jogada(self, play):
        #if play == "A1" :
            #self.tabuleiro[0][0] = jogador1.token

    #def validarjogada(self, play):
        


##Introducao de dados
##Jogador 1
jogador1 = jogador()
jogador1.nome = input("[Jogador 1] Nome do jogador: ")
jogador1.token = input("[Jogador 1] Token que prente usar: ")
##Jogador 2
jogador2 = jogador()
jogador2.nome = input("[Jogador 2] Nome do jogador: ")
jogador2.token = input("[Jogador 2] Token que prente usar: ")

##Tabuleiro
tabuleiro1 = tabuleiro()
jogador1.validar_jogador()    
tabuleiro1.__str__()

##Jogada
play = input('Insira onde quer realizar a sua jogada: ')