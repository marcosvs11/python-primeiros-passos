sep = 30 * '='
tit = 'VIEIRAS BUS'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        km = int(input('Digite a distância do destino em KM: '))
        if km > 200:
            kmida = km * 0.45
            print(f'lembrando que por km será cobrado R$0,45.')
            print(f'O valor da viagem será de R${kmida:,.2f}!')
            volta = input('Quer calcular o valor da passagem de volta? (s/n): ').strip()
            if volta.lower() != 'n':
                kmvolta = (km * 0.50) + kmida
                print('OBS: O valor cobrado pela passagem de volta é de R$0,50 por km.')
                print(f'O valor final com passagens ida e volta será de R${kmvolta:,.2f}!')
        elif km <= 200:
            kmida = km * 0.50
            print(f'lembrando que por km será cobrado R$0,50.')
            print(f'O valor da passagem será de R${kmida:,.2f}!')
            volta = input('Quer calcular o valor da passagem de volta? (s/n): ').strip()
            if volta.lower() != 'n':
                kmvolta = (km * 0.55) + kmida
                print('OBS: O valor cobrado pela passagem de volta é de R$0,55 por km.')
                print(f'O valor final com passagens ida e volta será de R${kmvolta:,.2f}!')
        resp = input('Quer comprar passagens para um destino diferente? (s/n): ').strip()
        if resp != 's':
            print('Compras finalizadas!')
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números! Tente novamente.')