from time import sleep
sep = 30 * '='
tit = 'Conversão Numérica'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        num = int(input('Digite um número inteiro: '))
        print('1 - Converter para BINÁRIO')
        print('2 - Converter OCTAL')
        print('3 - Converter HEXADECIMAL')
        opcao = int(input('Escolha um tipo de conversão: '))
        if opcao == 1:
            conversao = bin(num)
            escolhido = 'binário'
        elif opcao == 2:
            conversao = oct(num)
            escolhido = 'octal'
        elif opcao == 3:
            conversao = hex(num)
            escolhido = 'hexadecimal'
        print(f'O número {num} convertido para {escolhido} é igual a {conversao[2:]}')
        resp = input('Deseja outra opção de conversão: (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números!')
        print('Tente novamente.')