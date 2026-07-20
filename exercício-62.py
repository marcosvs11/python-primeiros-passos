try:
    sep = 30 * '='
    tit = 'Calculadora de P.A.'.center(30, ' ')
    print(sep)
    print(tit)
    print(sep)
    n1 = int(input('Digite o 1°termo: '))
    razao = int(input('Digite o valor da razão: '))
    resultado = n1
    quant_termos = 10 
    while quant_termos != 0:
        cont = 0
        while cont < quant_termos:
            cont += 1
            if cont == quant_termos:
                print(resultado, end='')
            else:    
                print(resultado, end=', ') 
                resultado += razao
        print(f'\nFIM DOS {quant_termos}° TERMOS!')
        quant_termos = int(input('Quantos termos será revelado agora? (número 0 para sair): '))
        if quant_termos == 0:
            print('Saindo...')
            break
except ValueError:
    print('Está pergunta aceita apenas números inteiros!')
    print('Tente novamente.')