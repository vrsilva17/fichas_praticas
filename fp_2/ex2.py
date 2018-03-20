num1 = int(input('Introduza o primeiro valor: '))
num2 = int(input('Introduza o segundo valor: '))
num3 = int(input('Introduza o terceiro valor: '))

if num1 > num2 and num2 > num3 :
    print(num1 ,num2, num3)
elif num1 > num3 and num3 > num2 :
    print(num1, num3, num2)
elif num2 > num1 and num1 > num3 :
    print(num2, num1, num3)
elif num2 > num3 and num3 > num1 :
    print(num2, num3, num1)
elif num3 > num2 and num2 > num1 :
    print(num3, num2, num1)
elif num3 > num1 and num1 > num2 :
    print(num3, num1, num2)