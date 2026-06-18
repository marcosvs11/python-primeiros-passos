import random
enter = ''
while enter != 'n':
    enter = input('Digite "ENTER" para continuar ou "N" para parar: ' )
    if enter == 'n':
        break
    print(f'Você tirou: {random.randint(1,6)}')

