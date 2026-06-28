resp = 's'
while resp != 'n':
    sep = 30*'='
    tit = 'Que Número Estou Pensando?'.center(30, ' ')
    print(sep)
    print(tit)
    print(sep)
    esco = 3
    tent = int(input('Digite o número: '))
    if tent == esco:
        print('Parabéns, você acertou o número!')
        break
    else:
        print('Vish...Parece que você digitou o número incorreto!')
        resp = input(('Quer tentar novamente? (s/n): ')).strip()
        if resp.lower() != 's':
            print('Ah, que pena...Achei que você iria conseguir acertar!')
            break