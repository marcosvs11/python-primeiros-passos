sep = 30 * '='
tit = 'Ano Bissexto ou Não?'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        abi = int(input('Digite um ano qualquer: '))
        if abi % 4 == 0:
            if abi % 100 == 0:
                if abi % 400 == 0:
                    print(f'O ano {abi} é bissexto!')
                else:
                    print(f'O ano {abi} NÃO é bissexto!')
            else:
                print(f'O ano {abi} é bissexto!')
        else:
            print(f'O ano {abi} NÃO é bissexto!')
        resp = input('Quer tentar novamente com o ano diferente? (s/n): ').strip()
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números! Tente novamente.')