resp = 's'
while (resp != 'n'):
    try:
        sep = '='*30
        tit = 'Pintando o Quarto'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        larg = float(input('Digite a largura da parede: '))
        alt = float(input('Digite a altura da parede: '))
        area = larg * alt
        print()
        print(f'Essa parede tem {area:.2f}m²')
        print(f'Um litro de tinta pinta 2m²')
        totlitros = area / 2
        print(f'Ou seja, você precisará de {totlitros:.2f} litros para pintar está parede!')
        print()
        resp = input('Você quer medir a outra parade? (s/n): ')
        if (resp.lower() != 's'):
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')