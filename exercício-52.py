from sys import exit
from math import sqrt
sep = 30 * '='
tit = 'Número Primo?'.center(30, ' ')
resp = 's'
try:
    print(sep)
    print(tit)
    print(sep)
    num = int(input('Digite um número: '))
    primo = 'VERDADEIRO: É um Número Primo!'
    n_primo = 'FALSO: Não é um Número Primo!'
    limite = int(sqrt(num))
    if num <= 1:
        descisao = n_primo
    elif num == 2:
        descisao = primo
    elif num % 2 == 0:
        descisao = n_primo
    else:
        for i in range(3, limite + 1, 2):
            if num % i == 0:
                descisao = n_primo
                print(f'{descisao}')
                exit()
        descisao = primo
    print(f'{descisao}')
except ValueError:
    print('Está pergunta aceita apenas números!')
    print('Tente novamente!')