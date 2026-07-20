try:
    sep = 30 * '='
    tit = 'Calculadora de P.A.'.center(30, ' ')
    print(sep)
    print(tit)
    print(sep)
    n1 = int(input('Digite o 1°termo: '))
    razao = int(input('Digite o valor da razão: '))
    resultado = n1
    # 1° loop será os 10 primeiros termos.
    quant_termos = 10
    # Condição para repetir até o usuário sair.
    while quant_termos != 0:
        cont = 0
        # Usuário decide quantos termos mostrar.
        while cont < quant_termos:
            cont += 1
            # Para tirar a "," do último número.
            if cont == quant_termos:
                print(resultado, end='')
            else:    
                print(resultado, end=', ') 
                resultado += razao
        print(f'\nFIM DOS {quant_termos}° TERMOS!')
        # Ele decide a quantidade de termos.
        quant_termos = int(input('Quantos termos será revelado agora? (número 0 para sair): '))
        # Condição para o programa parar.
        if quant_termos == 0:
            print('Saindo...')
            break
except ValueError:
    print('Está pergunta aceita apenas números inteiros!')
    print('Tente novamente.')