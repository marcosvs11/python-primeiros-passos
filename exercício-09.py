resp = 's'
while(resp != 'n'):
    try:
        sep = '='*30
        tit = 'Tabuada do Marcos'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        n1 = int(input('Digite a tabuada desejada: '))
        print(f'{n1} X 1 = {n1*1}\n{n1} X 2 = {n1*2}\n{n1} X 3 = {n1*3}\n{n1} X 4 = {n1*4}\n{n1} X 5 = {n1*5}\n{n1} X 6 = {n1*6}\n{n1} X 7 = {n1*7}\n{n1} X 8 = {n1*8}\n{n1} X 9 = {n1*9}\n{n1} X 10 = {n1*10}')
        resp = input('Quer tentar com outro número? (s/n): ')
        if (resp.lower != 's'):
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')