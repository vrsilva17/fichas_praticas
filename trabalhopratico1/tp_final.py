from tp_jogador import Jogador
from tp_tabuleiro import Tabuleiro
from tp_jogo import Jogo

class Final():

    def menu(self):       
        print(30 * "-" , "MENU" , 30 * "-")
        print("1. Criar novo jogador")
        print("2. Jogar")
        print("3. Ver pontuação")
        print("4. Exit")
        print(67 * "-")


    def escolha(self):
        opcao = None
        while opcao != "4":
            self.menu()
            opcao = input("Escolha uma das opções do menu acima ilustrado: ")
            if opcao == "1":
                p1 = Jogo()
                p1.inserir_jogador()
                token = input("Escolha o seu token: ")
                p1.inserir_token(token)
                print(p1)
            elif opcao == "2":
                t1 = Tabuleiro()
                print(t1)
                t1.jogar()
            elif opcao == "3":
                print("Ranking")
        exit

if __name__ == "__main__":

    f1 = Final()   
    f1.escolha()

