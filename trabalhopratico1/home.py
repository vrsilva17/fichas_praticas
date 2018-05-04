class Jogador():

    def __init__(self, nome, token):
        self.nome = nome
        self.token = token
    
    def __str__(self):
        return "Nome do jogador: {} \n Token: {}".format(self.nome, self.token)

class Tabuleiro():

    def __init__(self):
        self.data = [ [" "," "," "], 
                      [" "," "," "], 
                      [" "," "," "] ]
    
    def __str__(self):
        return str(self.data[1][1])

    
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


teste = Tabuleiro()      
print (teste)



