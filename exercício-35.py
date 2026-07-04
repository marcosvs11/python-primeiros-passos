from time import sleep
sep = 30 * '='
tit = 'Empréstimo Bancário'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        val_casa = float(input('Digite o valor da casa: R$'))
        sal = float(input('Digite o seu salário atual: R$'))
        pag_anos = int(input('Digite a quantidade de anos para pagar: '))
        meses = pag_anos * 12
        prest = val_casa / meses
        condição = sal * 0.30
        print(f'Valor da prestação: {meses}x R${prest:,.2f} ')
        print('Processando...')
        sleep(2)
        if prest > condição:
            print('EMPRÉSTIMO NEGADO!')
            print('Salário insuficiente, pois a prestação excede 30% da sua renda!')
        else:
            print('PARABÉNS, EMPRÉSTIMO APROVADO!')
            print('O sonho de casa própria está mais perto que nunca!')
        resp = input('Quer simular as prestações novamente? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números!')
        print('Tenete novamente.')