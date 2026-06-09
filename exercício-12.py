resp = 's'
while(resp != 'n'):
    try:
        sep = '='*30
        tit = 'Mercado do Marcos'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        print('Para compras até R$99,99 -> 5% de desconto')
        print('Para compras acima de R$100,00 -> 10% de desconto')
        print('Para compras acima de R$300,00 -> 15% de desconto')
        print('Para compras acima de R$900,00 -> 25% de desconto')
        print('-'*55)
        comptot = float(input('Digite o valor total da sua compra(somente números): '))
        if (comptot < 100):
            comptot = comptot * 0.95
            print('Os seus produtos receberam 5% de desconto do valor total!')
            print(f'O valor final da compra foi de R${comptot:.2f}.')
        elif (comptot < 300):
            comptot = comptot * 0.90
            print('Os seus produtos receberam 10% de desconto do valor total!')
            print(f'O valor final da compra foi de R${comptot:.2f}.')
        elif (comptot < 900):
            comptot = comptot * 0.85
            print('Os seus produtos receberam 15% de desconto do valor total!')
            print(f'O valor final da compra foi de R${comptot:.2f}.')
        elif (comptot >= 900):
            comptot = comptot * 0.75
            print('Os seus produtos receberam 25% de desconto do valor total!')
            print(f'O valor final da compra foi de R${comptot:.2f}.')

        resp = input('Quer tentar novamente com outro número? (s/n): ')
        if (resp.lower() != 's'):
            print('Saindo...')
            break

    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')