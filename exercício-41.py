from datetime import date
from time import sleep
sep = 30 * '='
tit = 'Qual a Sua Categoria?'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        nasc = int(input('Digite o ano de nascimento: '))
        ano = date.today().year
        idade = ano - nasc
        print('PROCESSANDO...')
        sleep(2)
        if idade <= 9:
            categoria = 'mirim'
        elif idade <= 14:
            categoria = 'infantil'
        elif idade <= 19:
            categoria = 'junior'
        elif idade <= 20:
            categoria = 'sênior'
        elif idade > 20:
            categoria = 'master'
        print(f'Você tem {idade} anos e se encaixa categoria {categoria}!')
        resp = input('Quer tentar novamente com outra data? (s/n): ').strip().lower()
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números!')
        print('Tente novamente.')