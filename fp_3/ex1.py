num = int(input('Introduza um numero: '))

print('Anteriores: ')
for a in range(num -1, num -6, -1):
    print(a, end=" ")
    
print('\nSeguintes: ')
for b in range(num +1, num +6, 1):
    print(b, end=" ")
