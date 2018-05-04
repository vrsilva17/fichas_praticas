import random

def listar(myList):
    for i in range(len(myList)):
        print(myList[i],end=" ")
        
grades = random.sample(range(0, 100), 20)

listar(grades)
print('\n')
