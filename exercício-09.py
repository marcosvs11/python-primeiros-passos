resp = 's'
while(resp != 'n'):
    try:
        sep = '='*30
        tit = 'Tabuada do Marcos'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        n1 = int(input('Digite a tabuada desejada: '))
        for i in range(1, 11):
            mult = n1 * i
            print(f'{n1} X {i} = {mult}')
        resp = input('Quer tentar com outro número? (s/n): ')
        if (resp.lower() != 's'):
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')