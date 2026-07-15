from time import sleep
sep = 30 * '='
tit = 'Calculadora Vieira'.center(30, ' ')
resp = 's'
while True:
    try:
        while resp != 'n':
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
            resp = 'n'
        sleep(1)
        print(sep)
        print(tit)
        print(sep)
        print('[ 1 ] Somar')
        print('[ 2 ] Subtrair')
        print('[ 3 ] Multiplicar')
        print('[ 4 ] Outros Números')
        print('[ 5 ] Sair do Programa')
        opcao = int(input('Digite a sua opção: '))
        if opcao == 1:
            operacao = f'{n1} + {n2} = '
            resultado = n1 + n2
        elif opcao == 2:
            operacao = f'{n1} - {n2} = '
            resultado = n1 - n2
        elif opcao == 3:
            operacao = f'{n1} x {n2} = '
            resultado = n1 * n2
        elif opcao == 4:
            print('Retornando a escolha dos números...')
            sleep(1)
            resp = 's'
            continue
        elif opcao == 5:
            print('Saindo...')
            sleep(1)
            break
        print(f'RESULTADO: {operacao}{resultado}.')
        sleep(1)
        print('Voltando para o menu...')
        continue
    except ValueError:
        print('Está pergunta aceita apenas números, tente novamente!')