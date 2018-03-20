nota1 = float(input('Introduza a primeira nota: '))
nota2 = float(input('Introduza a segunda nota: '))
nota3 = float(input('Introduza a terceira nota: '))

media = (nota1 * 25 + nota2 * 35 + nota3 * 40)/100

if media < 9.5 :
    print('O aluno não aprovado')
else:
    print('Aluno aprovado')