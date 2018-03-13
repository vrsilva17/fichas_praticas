nota1 = float(input('Introduza a sua primeira nota: '))
nota2 = float(input('Introduza a sua segunda nota: '))
nota3 = float(input('Introduza a sua terceira nota: '))

media = float(nota1 * 0.25 + nota2 * 0.35 + nota3 * 0.4)
media_int = int((nota1 * 25 + nota2 * 35 + nota3 * 40) //100)
media_mod = int((nota1 * 25 + nota2 * 35 + nota3 * 40)%100)

print('Média:', media)
print('Media inteira: ', media_int)
print('Media modulo: ', media_mod)
