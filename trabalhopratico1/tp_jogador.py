class Jogador():

    def __init__(self):
        self.nome = None
        self.token = None

    def __str__(self):
        return "Nome do jogador: {} \n Token escolhido: {}".format(self.nome, self.token)

if __name__ == "__main__": 

    j1 = Jogador()
    j1.nome = input("Insira o seu nome: ")
    j1.token = input("Insira o seu token:  ")
    j2 = Jogador()
    j2.nome = input("Insira o seu nome:  ")
    j2.token = input("Insira o seu token:  ")

    print(j1)  
    print(j2)
    