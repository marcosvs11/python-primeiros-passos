resp = 's'
while(resp != 'n'):
    try:
        sep = '='*30
        tit = 'Conversor de Moedas'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        nome = input('Digite o seu nome: ').upper()
        din = float(input('Digite a quantidade de dinheiro em reais que você possui: '))
        if (din < 0):
            print('Impossível converter números negativos. Tente novamente!')
        else: 
            print(f'Seu nome é {nome}')
            print(f'Possui R${din:.2f}')
            print(f'Convertendo ${din/5.04:.2f}')
            print(f'Convertendo €{din/5.90:.2f}')
            print()
            resp = input('Quer mudar o valor do seu patrimônio? (s/n): ')
            if (resp.lower() != 's'):
                print('Saindo...')
                break
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')