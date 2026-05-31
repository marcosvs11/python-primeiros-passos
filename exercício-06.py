resp = 's'
while(resp != 'n'):  
    try:
        sep = '='*30
        tit = 'D.T.R.'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        n1 = float(input('Digite um número: '))
        print()
        print(f'Número escolhido: {n1}')
        print(f'O dobro: {n1*2:.2f}')
        print(f'O tripo: {n1*3:.2f}')
        print(f'A raiz quadrada: {n1**(1/2):.2f}')
        print(f'A raiz cúbica: {n1**(1/3):.2f}')
        print()
        resp = input('Quer continuar com outro número? (s/n): ')
        if(resp.lower() != 's'):
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas NÚMEROS. Tente novamente!')