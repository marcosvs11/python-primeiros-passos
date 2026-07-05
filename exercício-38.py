from time import sleep
sep = 30 * '='
tit = 'Quem é o Maior?'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('Em análise...')
        sleep(2)
        if n1 > n2:
            print(f'O primeiro número é maior que o segundo, ou seja, {n1} > {n2}.')
        elif n2 > n1:
            print(f'O segundo número é maior que o primeiro, ou seja, {n2} > {n1}.')
        elif n1 == n2:
            print(f'Tanto o primeiro número quanto o segundo, possuem o mesmo valor!')
        sleep(2)
        resp = input('Quer tentar novamente com números diferentes? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números!')
        print('Tente novamente.')