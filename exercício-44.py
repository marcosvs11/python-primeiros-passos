from time import sleep
from sys import exit
sep = 30 * '='
tit = 'Mercado Vieira'.center(30, ' ')
produtos = ['Arroz (5kg) - R$20,00', 'Feijão (1kg) - R$12,00', 'Alface (250g) - R$10,00', ' Bife de Coxão Mole (1kg) - R$42,00']
try:
    print(sep)
    print(tit)
    print(sep) 
    for i in range(4):
        produtos[i] = print(f'[{i + 1}] {(produtos[i].strip())}')
    escolha = int(input('Digite o número do seu pedido: '))
    if escolha == 1:
        item = 'Arroz 5kg'
        valor = 20
    elif escolha == 2:
        item = 'Feijão 1kg'
        valor = 12
    elif escolha == 3:
        item = 'Alface'
        valor = 10
    elif escolha == 4:
        item = '1kg de Bife de Coxão Mole'
        valor = 42
    else:
        print('Opção Inválida!')
        exit()
    print()
    print('FINALIZANDO A COMPRA...')
    sleep(2)
    print()
    print(f'Item escolhido: {item}')
    print(f'Valor Total: R${valor:,.2f}')
    print()
    print('UM MOMENTO...')
    sleep(2)
    print()
    print('''Forma de pagamento: 
[1] Dinheiro/Pix -> 10% de desconto
[2] Cartão à Vista -> 5% de desconto
[3] Cartão Parcelado -> 2x s/ juros
[0] Cancelar''')
    opcao = int(input('Digite a sua opção: '))
    print()
    if opcao == 1:
        metodo = 'Dinheiro/Pix'
        desc = '10% de desconto'
        v_final = valor * 0.90
    elif opcao == 2:
        metodo = 'Cartão à Vista'
        desc = '5% de desconto'
        v_final = valor * 0.95
    elif opcao == 3:
        parc = int(input('Digite quantas vezez o parcelamento (máx 10x): '))
        if parc > 10 or parc < 0:
            print('Parcelamento até 10x!')
            print('Tente novamente')
            exit()
        metodo = 'Cartão Parcelado'
        desc = f'{parc}x' 
        if parc > 2:
            print('OBS: Mais de 2x serão acrescentadas 20% de juros por parcela excedente!')
            v_integral = valor * (1.20 **(parc - 2))
            v_final = v_integral / parc
            v_final = f'{v_final:,.2f} em {parc}x -> R${v_integral:,.2f}'
        else:
            v_integral = valor
            calc = valor / parc
            v_final = f'{calc:,.2f} cada parcela -> {v_integral:,.2f}'
    elif opcao == 0:
        print('CANCELANDO...')
        exit()
    else:
        print('Opção Inválida!')
        exit()
    print('CALCULANDO...')
    sleep(2)
    print()
    print(f'Forma de Pagamento: {metodo} -> {desc}')
    print(f'Valor Final: R${v_final}')
    print(f'Compra Finalizada!')
except ValueError:
    print('Está pergunta aceita apenas números!')