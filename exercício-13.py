resp = 's'
while(resp != 'n'):
    try:
        sep = '='*30
        tit = 'Reajuste Salarial - 2026'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)    
        sal_atual = float(input('Digite o valor do seu salário atual: '))
        if(sal_atual <= 0):
            print('Impossível calcular esse salário. Tente novamente!')
        else:
            print()
            print('Escolha a opção em que você se enquadra.'.center(30, ' '))
            print()
            print('1 - Aumento de 6,79% referente ao salário mínimo.')
            print('2 - Aumento de 3,90% referente aos aposentados/pensionistas acima do mínimo.')
            print('3 - Porcentagem personalizada pelo sindicato.')
            opcao = int(input('Digite a opção: '))
            if(opcao == 1):
                sal_novo = sal_atual * (6.79 / 100) + sal_atual 
                print(f'O seu salário reajustado é de R${sal_novo:,.2f}.')
            elif(opcao == 2):
                sal_novo = sal_atual * (3.90 / 100) + sal_atual
                print(f'O seu salário reajustado da aposentadoria/pensão é de R${sal_novo:,.2f}.')
            elif(opcao == 3):
                porct = float(input('Digite o valor da porcentagem personalizada: '))
                if (porct <= 0 or porct > 100):
                    print('Por gentileza, digite uma porcentagem entre 0 a 100.')
                else:
                    sal_novo = sal_atual * (porct / 100) + sal_atual
                    print(f'O seu salário reajustado é de R${sal_novo:,.2f}.')
            else:
                print('Opção inválida. Escolha apenas as opções destacadas!')
            resp = input('Você quer tentar novamente com outro salário? (s/n): ')
            if(resp.lower() != 's'):
                print('Saindo...')
                break
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')