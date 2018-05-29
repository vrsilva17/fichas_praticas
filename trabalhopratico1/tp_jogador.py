class Jogador():

    def __init__(self, nome, token):
        self.nome = nome
        self.token = token

    def __str__(self):
        return "Nome do jogador: {} \n Token escolhido: {}".format(self.nome, self.token)
    
    def validar_token(self):
        while j1.token == j2.token:
            print("Token repetido!")
            j2.token = input("{} escolha outro token:  ".format(j2.nome))
        return j2.token


if __name__ == "__main__": 

    j1 = Jogador("Vitor","X")
    j2 = Jogador("Hugo", "X")

    j1.validar_token()

    print(j1)  
    print(j2)

    