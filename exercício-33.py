try:
    sep = 30 * '='
    tit = 'Reajuste Salarial'.center(30, ' ')
    print(sep)
    print(tit)
    print(sep)
    sal = float(input('Digite seu salário: '))
    sal_min = 1621
    if sal > sal_min:
        sal_nv = sal * 1.10
        dif = sal_nv - sal
        print(f'Seu salário recebeu um acréscimo de 10%, resultando em R${dif:,.2f} a mais!')
        print(f'Ou seja, sai de R${sal:,.2f} para R${sal_nv:,.2f}!')
    elif sal <= sal_min:
        sal_nv = sal * 1.15
        dif = sal_nv - sal
        print(f'Seu salário recebeu um acréscimo de 15%, resultando em R${dif:,.2f} a mais!')
        print(f'Ou seja, sai de R${sal:,.2f} para R${sal_nv:,.2f}!')
except ValueError:
    print('Está pergunta aceita apenas números! Tente novamente.')