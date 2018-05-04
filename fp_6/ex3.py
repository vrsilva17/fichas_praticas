numeros = []
x = 0

def lista_cont(myList):
    for i in range(len(myList)):
        print(myList[i],end=" ")

def dobro(myList):
    for i in range(len(myList)):
        print(myList[i]*2,end=" ")

def soma(myList):
    sum = 0
    for numeros in myList:
        sum += numeros
    return sum 

def media(myList):
    sum = 0
    for numeros in myList:
        sum += numeros
    return sum /len(myList)


while x <= 10:
    n = int(input('Digite um número: '))
    numeros.append(n)
    x += 1

print('Conteúdo da lista:') 
lista_cont(numeros)
print('Dobro de cada elemento:') 
dobro(numeros)
print('Soma: ', soma(numeros))
print('Media: ', media(numeros))
print("Maior número: ", max(numeros))
print("Menor número: ", min(numeros))