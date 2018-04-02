cand1 = 0
cand2 = 0
cand3 = 0
cand4 = 0
vbranco = 0
vnulo = 0

print('Escolha uma das opçoes indicadas abaixo:')
print('-1- Terminar a contagem')
print('0- Votar em branco')
print('1- Votar no Candidato 1')
print('2- Votar no Candidato 2')
print('3- Votar no Candidato 3')
print('4- Votar no Candidato 4')
print('9- Votar nulo')
voto = int(input('Voto: '))

while voto != -1:
    if voto == 0:
        vbranco += 1
    if voto == 1:
        cand1 += 1
    if voto == 2:
        cand2 += 1
    if voto == 3:
        cand3 += 1
    if voto == 4:
        cand4 += 1
    if voto == 9:
        vnulo += 1

    print('Escolha uma das opçoes indicadas abaixo:')
    print('-1- Terminar a contagem')
    print('0- Votar em branco')
    print('1- Votar no Candidato 1')
    print('2- Votar no Candidato 2')
    print('3- Votar no Candidato 3')
    print('4- Votar no Candidato 4')
    print('9- Votar nulo')
    voto = int(input('Voto: '))

tvotos = cand1 + cand2 + cand3 + cand4 + vbranco + vnulo
p_cand1 = (cand1 * 100) / tvotos
p_cand2 = (cand2 * 100) / tvotos
p_cand3 = (cand3 * 100) / tvotos
p_cand4 = (cand4 * 100) / tvotos
p_vbranco = (vbranco * 100) / tvotos
p_vnulo = (vnulo * 100) / tvotos


print('O número total de votos é:', tvotos)
print('Candidato 1:       {}% ({} votos)'.format(p_cand1,cand1))
print('Candidato 2:       {}% ({} votos)'.format(p_cand2,cand2))
print('Candidato 3:       {}% ({} votos)'.format(p_cand3,cand3))
print('Candidato 4:       {}% ({} votos)'.format(p_cand4,cand4))
print('Votos em branco:   {}% ({} votos).'.format(p_vbranco,vbranco))
print('Votos nulos:       {}% ({} votos).'.format(p_vnulo,vnulo))