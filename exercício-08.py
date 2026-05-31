resp = 's'
while(resp != 'n'):
    try:
        sep = '='*30
        tit = 'Conversor de Medidas'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        med = float(input('Digite uma medida em metros(apenas números): '))
        print()
        km = med / 1000
        cm = med * 100
        mm = med * 1000
        print(f'{med} Metros para Quilômetros: {km:.3f}')
        print(f'{med} Metros para Centímetros: {cm:.2f}')
        print(f'{med} Metros para Milímetros: {mm:.2f}')
        print()
        resp = input('Quer tentar com outro número? (s/n): ')
        if (resp.lower != 's'):
            print('Saindo...')
            break
    except ValueError:
        print('Este progama aceita apenas números. Tente novamente!')