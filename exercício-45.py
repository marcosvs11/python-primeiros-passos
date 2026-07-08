import random
from time import sleep
sep = 30 * '='
tit = 'Jokenpô'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        jokenpo = ['Pedra', 'Papel', 'Tesoura']
        compt = random.choice(jokenpo)
        print('''[1] - Papel
[2] - Pedra
[3] - Tesoura''')
        opcao = int(input('Digite a sua opção: '))
        if opcao == 1:
            usua = 'Papel'
        elif opcao == 2:
            usua = 'Pedra'
        elif opcao == 3:
            usua = 'Tesoura'
        if usua == compt:
            result = 'EMPATE'
            msg = 'Que pena, eu queria ganhar!'
        else:
            if usua == 'Papel' and compt == 'Pedra' or usua == 'Pedra' and compt == 'Tesoura' or usua == 'Tesoura' and compt == 'Papel':
                result = 'VITÓRIA'
                msg = 'Parabéns, você ganhou de mim!'
            elif usua == 'Papel' and compt == 'Tesoura' or usua == 'Tesoura' and compt == 'Pedra' or usua == 'Pedra' and compt == 'Papel':
                result = 'DERROTA'
                msg = 'Fraco, tente mais uma vez!'
        print()
        print('CARREGANDO RESULTADO...')
        print()
        sleep(2)
        print(f'Eu escolhi {compt}.')
        print(f'E você {usua}.')
        print(f'Resultado: {result}.')
        print(f'{msg}')
        sleep(1)
        print()
        resp = input('Quer tentar novamente? (s/n): ').strip().lower()
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números!')
        print('Tente novamente.')