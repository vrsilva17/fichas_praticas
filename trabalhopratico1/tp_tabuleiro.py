from tp_jogador import Jogador

class Tabuleiro():

    def __init__(self):
        self.lista_tabuleiro = [ [None, None, None],
                                 [None, None, None],
                                 [None, None, None] ]
    
    def __str__(self):
        _str = "  A  B  C"
        for i in range (0, 3):
            _str += "\n" + str(i+1)
            for j in range (0, 3):
                if self.lista_tabuleiro[i][j] == None:
                    _str += "  |" 
                else:
                    _str += " " + self.lista_tabuleiro[i][j] + "|"
        return _str


    def validar_jogada(self, play, token):        
        if (play[0] == "A" or play[0] == "B" or play[0] == "C") and (play[1] == "1" or play[1] == "2" or play[1] == "3"):
            if play[0] == "A":
                j = 0
                i = int(play [1]) - 1
                if self.lista_tabuleiro[i][j] == None:
                    self.lista_tabuleiro[i][j] = token
                else:
                    return "Posição Ocupada"
                    self.validar_jogada(play,token)
            if play[0] == "B":
                j = 1
                i = int(play [1]) - 1
                if self.lista_tabuleiro[i][j] == None:
                    self.lista_tabuleiro[i][j] = token
                else:
                    return "Posição Ocupada"
                    self.validar_jogada(play,token)
            if play[0] == "C":
                j = 2
                i = int(play [1]) - 1
                if self.lista_tabuleiro[i][j] == None:
                    self.lista_tabuleiro[i][j] = token
                else:
                    return "Posição Ocupada"
                    self.validar_jogada(play,token)
        else:
            return "Posição Ocupada"
            self.validar_jogada(play,token)

    def vitoria(self, nome, token):
        if  (self.lista_tabuleiro[0][0] == token and self.lista_tabuleiro[0][1] == token and self.lista_tabuleiro[0][2] == token) or \
            (self.lista_tabuleiro[1][0] == token and self.lista_tabuleiro[1][1] == token and self.lista_tabuleiro[1][2] == token) or \
            (self.lista_tabuleiro[2][0] == token and self.lista_tabuleiro[2][1] == token and self.lista_tabuleiro[2][2] == token) or \
            (self.lista_tabuleiro[0][0] == token and self.lista_tabuleiro[1][0] == token and self.lista_tabuleiro[2][0] == token) or \
            (self.lista_tabuleiro[1][0] == token and self.lista_tabuleiro[1][1] == token and self.lista_tabuleiro[1][2] == token) or \
            (self.lista_tabuleiro[2][0] == token and self.lista_tabuleiro[2][1] == token and self.lista_tabuleiro[2][2] == token) or \
            (self.lista_tabuleiro[0][0] == token and self.lista_tabuleiro[1][1] == token and self.lista_tabuleiro[2][2] == token) or \
            (self.lista_tabuleiro[2][0] == token and self.lista_tabuleiro[1][1] == token and self.lista_tabuleiro[0][2] == token):
            global vencedor
            vencedor = True
        return True
    
    def jogar(self):
        vencedor = False
        count = 0
        while count <= 9:
            play = input("Insira a sua jogada: ")
            self.validar_jogada(play,"X")
            self.vitoria("Vitor","X")
            print(self)
            if vencedor == True:
                print("O vencedor é Vitor")
            count += 1
            if count == 9:
                print("Empate")
            play = input("Insira a sua jogada: ")
            self.validar_jogada(play,"O")
            self.vitoria("Silva","O")
            print(self)
            count += 1


        
if __name__ == "__main__":


    t1 = Tabuleiro()
    print(t1)

    t1.jogar()


    


    

    
