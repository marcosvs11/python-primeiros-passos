from time import sleep
sep = 30 * '='
tit = 'Qual o Fatorial?'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        n1 = int(input('Digite um número: '))
        print('PROCESSANDO...')
        sleep(2)
        if n1 < 0:
            print('Número indeterminado. Tente novamente!')
            continue
        resultado = 1
        origem = n1
        while n1 > 0:
            resultado *= n1
            n1 -= 1
        print(f'{origem}! = ', end='')
        for i in range(origem, 0, -1):
            if i == 1:
                print(f'{i}', end='')
            else:
                print(f'{i}x', end='')
        print(f' = {resultado}')
        if origem == 0:
            print(f'💡 -> O resultado de {n1}! é 1, pois é a única forma de separar 1 objeto!')
        sleep(1)
        resp = input('Quer tentar novamente com outro número? (s/n): ').strip().lower()
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números inteiros!')
        print('Tente novamente.')