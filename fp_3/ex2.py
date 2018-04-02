num = int(input('Introduza um valor: '))

if num == 2 :
    print('O número é primo')
else:
    while num > 1:
        for i in range(2, num):
            if num % i == 0:
                print('O número não é primo')
                break
            else:
                print('O número é primo')
                break
        break

if num <= 1:
    print('ERRO!') 