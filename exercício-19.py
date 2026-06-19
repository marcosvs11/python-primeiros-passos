import math
import random
resp = 's'
while resp != 'n':
    try:
        sep = 30*'='
        tit = 'Cos - Sen - Tg'.center(30, ' ')
        print(sep)
        print(tit)
        print(sep)
        ang = float(input('Digite um ângulo até 180°: '))
        rad = math.radians(ang)
        sen = math.sin(rad)
        cos = math.cos(rad)
        tg = math.tan(rad)
        print(f'Ângulo digitado: {ang}°') 
        print(f'Cosseno: {cos:.3f}')
        print(f'Seno: {sen:.3f}') 
        print(f'Tangente: {tg:.3f}')
        print()
        resp = input('Quer tentar novamente? (s/n): ')
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')