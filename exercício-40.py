#Para deixar a sensação do cálculo sendo feito.
from time import sleep
sep = 30* '='
tit = 'Escola Vieira'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        n1 = float(input('Digite a primeira nota: '))
        if n1 > 10:
            print('A nota máxima é 10 pontos! Tente novamente.')
            continue
        n2 = float(input('Digite a segunda nota: '))
        if n2 > 10:
            print('A nota máxima é 10 pontos! Tente novamente.')
            continue
        m = (n1 + n2) / 2
        print('Processando dados...')
        sleep(2)
        print(f'Média = {m:.2f}')
        if m < 5:
            print('REPROVADO!')
            print(f'Nota média inferior a 5.')
        elif m >= 5 and m < 7:
            print('RECUPERAÇÃO!')
            print(f'Nota média entre 5 e 6.9.')
        elif m >= 7:
            print('APROVADO!')
            print(f'Parabéns pela média superior a 6.9.')
        resp = input('Quer tentar novamente com outras notas? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Este número aceita apenas números!')
        print('Tente novamente.')