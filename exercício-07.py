resp = 's'
while(resp != 'n'):
    try:
        sep = '='*30
        tit = 'Escola Marcos Dev'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        nome = input('Escreva o nome do aluno: ').upper()
        n1 = float(input(f'Digite a sua nota na matéria de portuguẽs: '))
        if (n1 > 10 or n1 < 0):
            print('A nota máxima é 10 (dez) e a mínima é 0 (zero). Tente novamente!')
        else:
            n2 = float(input(f'Digite também a nota em matemática: '))
            if (n2 > 10 or n2 < 0):
                print('A nota máxima é 10 (dez) e a mínima é 0 (zero). Tente novamente!')
            else:
                m = (n1+n2) / 2
                print()
                print(f'Nome: {nome}')
                print(f'Nota em português: {n1:.2f}')
                print(f'Nota em matemática: {n2:.2f}')
                print(f'E a média final: {m:.2f}')
                print()
                if (m >= 6.5):
                    print('PARABÉNS, VOCÊ FOI APROVADO!')
                else:
                    print('REPROVADO, TENTE NOVAMENTE!')
                print()
                resp = input('Você quer refazer a prova? (s/n): ')
                if (resp.lower() != 's'):
                    print('Saindo...')
                    break
    except ValueError:
        print('Este programa aceita apenas números como notas. Tente novamente!')