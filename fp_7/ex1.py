import random 

NUM_VALORES = 30
VALOR_MAX = 100

file = open("teste.txt", "a")

for i in range(0,NUM_VALORES):
    a = str(random.randint(0,VALOR_MAX)) + "\n" 
    file.write(a)

file.close()