from random import randint
resp = 's'
esco = randint(0, 5)
while resp != 'n':
    sep = 30*'='
    tit = 'Que Número Estou Pensando?'.center(30, ' ')
    print(sep)
    print(tit)
    print(sep)
    print('DICA: Entre 0 e 5.')
    tent = int(input('Digite o número: '))
    dist = abs(esco - tent)
    if tent == esco:
        print('Parabéns, você acertou o número!')
        resp = input('Quer tentar novamente? (s/n): ')
        esco = randint(0, 5)
        if resp != 's':
            print('Espero que tenha gostado!')
            print('Saindo...')
            break
    else:
        if dist > 4:
            temp = 'Está gelado...'
        elif dist == 3 or dist == 2:
            temp = 'Está tão perto...'
        elif dist == 1:
            temp = 'Está quentíssimo...'
        
        if tent < esco:
            direc = 'É um número maior.'
        elif tent > esco:
            direc = 'É um número menor.'

        print(temp)
        print(direc)