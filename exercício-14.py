def MostrarMenu():
    print('Escolha uma das unidades de medida: '. center(30, ' '))
    print('1 - Celsius (°C).')
    print('2 - Fahrenheit (°F).')
    print('3 - Kelvin (K).')
    print('0 - Sair')

resp = 's'
while (resp != 'n'):
    try:
        sep = '='*30
        tit = 'Conversor de Temperaturas'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        MostrarMenu()
        opcao = int(input('Digite sua opção: '))
        if (opcao > 3) or (opcao < 0):
            print('Erro. Digite uma das opções acima. Tente novamente!')
            continue
        if (opcao == 1): 
            cel = float(input('Digite a temperatura em celsius (°C): '))
            fah = (cel * 1.8) + 32
            kel = cel + 273.15
            print(f'Celsius (°C) -> Fahrenheit (°F): {fah:.2f}°F.')
            print(f'Celsius (°C) -> Kelvin (K): {kel:.2f}K.')

        elif (opcao == 2):
            fah = float(input('Digite a temperatura em fahrenheit (°F): '))
            cel = (fah - 32) / 1.8
            kel = (fah - 32) * 5/9 + 273.15
            print(f'Fahrenheit (°F) -> Celsius (°C): {cel:.2f}°C. ')
            print(f'Fahrenheit (°F) -> Kelvin (K): {kel:.2f}K')

        elif (opcao == 3):
            kel = float(input('Digite a temperatura em kelvin (K): '))
            cel = kel - 273.15
            fah = (kel - 273.15) * 1.8 + 32 

            print(f'Kelvin (K) -> Celsius (°C): {cel:.2f}°C.')
            print(f'Kelvin (K) -> Fahrenheit (°F): {fah:.2f}°F.')
        
        else:
            print('Saindo...')
            break
        resp = input('Vocễ quer tentar novamente? (s/n): ')
        if (resp.lower() != 's'):
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')