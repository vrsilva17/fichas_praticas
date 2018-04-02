nota1 = float(input('Introduza a primeira nota: '))
nota2 = float(input('Introduza a segunda nota: '))
nota3 = float(input('Introduza a terceira nota: '))

if nota1 < 0 or nota1 > 20 :
    print('A primeira nota é invalida')
elif nota2 < 0 or nota2 > 20 :
    print('A segunda nota é invalida')
elif nota3 < 0 or nota3 > 20 :
    print('A terceira nota é invalida')
else :
    media = (nota1 * 25 + nota2 * 35 + nota3 * 40)/100

    if media < 9.5 :
        print('O aluno não aprovado')
    else:
        print('Aluno aprovado')