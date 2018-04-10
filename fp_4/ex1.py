def login(utilizador, passw) :
    user = 'vitor'
    password = '123'

    if utilizador == user and passw == password :
        return True
    return False

def validar() :
    contar = 0
    while contar != 3 :
        v_user = input('User: ')
        v_password = input('Password: ')
        if login(v_user, v_password):
            print('Login efetuado')
            break
        else:
            print('ERRO !')
        contar += 1
        if contar >= 3 :
            print('Maximo de tentativas')
           
validar()
