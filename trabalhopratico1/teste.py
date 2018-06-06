def vencedor(tabuleiro,jogador):
    return vence_linhas(tabuleiro,jogador) or vence_colunas(tabuleiro, jogador) or vence_diagonais(tabuleiro, jogador)

def vence_linhas(tabuleiro,jogador):
    for i in range(len(tabuleiro)):
        vence = True
        for j in range(len(tabuleiro[0])):
            vence = vence and (tabuleiro[i][j] == jogador)
        if vence:
            return True
    return False
            
def vence_colunas(tabuleiro,jogador):
    for i in range(len(tabuleiro[0])):
        vence = True
        for j in range(len(tabuleiro)):
            vence = vence and (tabuleiro[j][i] == jogador)
        if vence:
            return True
        return False

def vence_diagonais(tabuleiro,jogador):
    vence_1 = True
    vence_2 = True
    for i in range(len(tabuleiro)):
        vence_1 = vence_1 and (tabuleiro[i][i] == jogador)
        vence_2 = vence_2 and (tabuleiro[i][len(tabuleiro)-1-i] == jogador)
    return vence_1 or vence_2