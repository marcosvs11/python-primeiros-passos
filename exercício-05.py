cont = 's'
while(cont.lower() != 'n'):
    try:    
        tit = 'Antecessor e Sucessor'.center(30, ' ')
        sep = '='*30
        print(sep)
        print(tit)
        print(sep)
        na = int(input('Digite um número: '))
        print(f'O antecessor de {na} é {na - 1} e o sucessor é {na + 1} ')
        cont = input('Quer continuar com outro número? (s/n): ')
        if cont.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('ERRO! Este programa aceita apenas números inteiros. Tente novamente!')