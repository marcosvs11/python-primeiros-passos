import math
try:
    sep = 50*'='
    tit = 'Qual o Comprimento da Hipotenusa?'.center(50, ' ')
    print(sep)
    print(tit)
    print(sep)
    ca = float(input('Digite o comprimento do cateto adjascente (em cm): '))
    co = float(input('Digite o comprimento do cateto oposto (em cm): '))
    print(f'O comprimento da hipotenusa é: {math.hypot(ca, co):.2f}cm')
    resp = input('Quer entender como realizar está operação? (s/n): ')
    if resp.lower() != 's':
        print('Saindo...')
    else:
        print(f'É simples, basta fazer o Teorema de Pitágoras: hip² = {co}² + {ca}² -> Resultando no valor {math.hypot(ca, co):.2f}cm')
except ValueError:
    print('Este programa aceita apenas números. Tente novamente!')