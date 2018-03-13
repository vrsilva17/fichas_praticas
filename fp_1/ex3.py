altura = float(input('Indique a sua altura em m: '))
peso = float(input('Indique o seu peso em kg: '))
imc = (peso / altura ** 2)

print('O seu indice de massa corporal é de: ', round(imc, 2))