def MostrarCarros():
    print('Carros Disponíveis: ')
    print('1 - Audi A3 | 2026')
    print('2 - BMW 320i | 2026')
    print('3 - Porsche 911 Turbo S | 2026')
    print('0 - Sair')

def CalculoAluguel(vcarro):
    dias = int(input('Digite por quantos dias você alugará o carro: '))
    vtotal = dias * vcarro
    print(f'O valor total gasto em alugel será de R${vtotal:,.2f}.')
resp = 's'
while (resp != 'n'):
    try:
        sep = '='*30
        tit = 'Aluguel de Carros'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        MostrarCarros()
        opcao = int(input('Digite a sua opção: '))
        if (opcao == 0):
            print('Saindo...')
            break

        if (opcao > 3) or (opcao < 0):
            print('Digite apenas os números destacados no menu. Tente novamente!')
            continue

        if (opcao == 1):
            vcarro = 350
            print()
            print('Audi A3 | 2026: '.center(30, ' '))
            print('Valor diário -> R$350,00')
            esc = input('Essa é a sua escolha final? (s/n): ')
            if (esc.lower() != 's'):
                print('Voltando para o menu...')
                continue
            CalculoAluguel(vcarro)

        elif (opcao == 2):
            vcarro = 1800
            print()
            print('BMW 320i | 2026: '.center(30, ' '))
            print('Valor diário -> R$1.800,00')
            esc = input('Essa é a sua escolha final? (s/n): ')
            if (esc.lower() != 's'):
                print('Voltando para o menu...')
                continue
            CalculoAluguel(vcarro)

        else:
            vcarro = 6500
            print()
            print('Porsche 911 Turbo S | 2026: '.center(30, ' '))
            print('Valor diário -> R$6.500,00')
            esc = input('Essa é a sua escolha final? (s/n): ')
            if (esc.lower() != 's'):
                print('Voltando para o menu...')
                continue
            CalculoAluguel(vcarro)
        resp = input('Quer alugar novamente? (s/n): ')
        if (resp.lower() != 's'):
            print('Saindo...')
            break    
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')