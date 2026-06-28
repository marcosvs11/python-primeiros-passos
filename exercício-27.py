from random import randint
resp = 's'
while resp != 'n':
    sep = 30*'='
    tit = 'Que Número Estou Pensando?'.center(30, ' ')
    print(sep)
    print(tit)
    print(sep)
    print('DICA: Entre 0 e 5.')
    esco = randint(0, 5)
    tent = int(input('Digite o número: '))
    if tent == esco:
        print('Parabéns, você acertou o número!')
        break
    else:
        print('Vish...Parece que você adivinhou o número incorreto!')
        print(f'O número que estava pensando era o {esco}.')
        resp = input(('Quer tentar novamente? (s/n): ')).strip()
        if resp.lower() != 's':
            print('Ah, que pena...Achei que você iria conseguir acertar!')
            break