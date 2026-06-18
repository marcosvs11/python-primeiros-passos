import random
resp = 's'
while resp != 'n':
    try:
        sep = 30*'='
        tit = 'Ordem de Apresentação'.center(30, ' ')
        quant = int(input('Quantos alunos estão no grupo? -> '))
        nomes = [''] * quant
        resp = 's'
        print(sep)
        print(tit)
        print(sep)
        for i in range(quant):
            nomes[i] = input(f'Digite o nome {[i+1]}: ')
        print(f'A ordem de apresentação é: {', '.join(random.sample(nomes, quant))}')
        print()
        resp = input('Quer sortear novamente com outros nomes? (s/n): ')
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Por gentileza, apenas NÚMEROS. Tente novamente!')    
