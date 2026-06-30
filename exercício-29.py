resp = 's'
sep = 30 * '='
tit = 'Par ou Ímpar?'.center (30, ' ')
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        num = int(input('Digite um número: '))
        if num % 2 != 0:
            print(f'O número {num} é IMPAR!')
        elif num % 2 != 1:
            print(f'O número {num} é PAR!')
        resp = input('Quer tentar outro número? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas números!')
        print('Tente novamente.')