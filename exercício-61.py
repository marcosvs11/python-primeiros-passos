from time import sleep
sep = 30 * '='
tit = 'Progressão Aritmética'.center(30, ' ')
try:
    print(sep)
    print(tit)
    print(sep)
    a1 = int(input('Digite o valor do 1° termo: '))
    razao = int(input('Digite o valor da razão: '))
    resultado = a1
    cont = 1
    print('PROCESSANDO...')
    sleep(1)
    # While para fazer o cálculo dos 10° termos.
    while cont <= 10:
        # Para tirar a seta do último número.
        if cont == 10:
            print(resultado, end='')
        else:
            print(resultado, end=' -> ')
        # Cálculo dos termos.
        resultado += razao
        cont += 1
    print('\nFim dos 10° termos!')
except ValueError:
    print('Está pergunta aceita apenas números!')
    print('Tente novamente.')