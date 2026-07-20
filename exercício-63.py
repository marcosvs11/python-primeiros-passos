from time import sleep
sep = 30 * '='
tit = 'Sequência de Fibonacci'.center(30, ' ')
resp = 's'
limite_fibonacci = 0
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        n1 = int(input('Digite um número inicial: '))
        limite_fibonacci = int(input('Digita a quantidade de termos revelados desejados: '))
        if limite_fibonacci <= 0:
            print('Número inválido, tente novamente!')
            continue
        print('PROCESSANDO...')
        sleep(1)
        atual = n1
        anterior = 0
        fibonacci = n1
        cont = 0
        while cont < limite_fibonacci:
            if cont + 1 == limite_fibonacci:
                print(fibonacci, end='')
            else:
                print(fibonacci, end=', ')
            fibonacci = atual + anterior
            anterior = atual
            atual = fibonacci
            cont += 1
        sleep(1)
        resp = input('\nVocê quer continuar com outro número? (s/n): ').lower().strip()
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números.\nTente novamente!')
