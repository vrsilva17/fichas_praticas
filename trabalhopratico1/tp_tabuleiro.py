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
        if play == "A1":
            j = 0
            i = 0
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        elif play == "A2":
            i = 1
            j = 0
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        elif play == "A3":
            i = 2
            j = 0
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        elif play == "B1":
            i = 0
            j = 1
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        elif play == "B2":
            i = 1
            j = 1
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        elif play == "B3":
            i = 2
            j = 1
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        elif play == "C1":
            i = 0
            j = 2            
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        elif play == "C2":
            i = 1
            j = 2            
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        elif play == "C3":
            i = 2
            j = 2
            if self.lista_tabuleiro[i][j] == None:
                self.lista_tabuleiro[i][j] = token
            else:
                return False
        else:
            return False

        #def vitoria(self):
        
if __name__ == "__main__":

    t1 = Tabuleiro()
    print(t1)

    for i in range(0,2):
        play = "A1"
        t1.validar_jogada(play,"X")
        print(t1)
    

    
