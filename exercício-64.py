from time import sleep
n1 = 0
cont = 1
soma = 0
sep = 30 * '='
tit = 'Somando Valores'.center(30, ' ')
print(sep)
print(tit)
print(sep)
while n1 != 999:
    try:
        n1 = int(input(f'Escolha o {cont}° número (digite 999 para sair): '))
        if n1 != 999:
            soma += n1
            cont += 1
    except ValueError:
        print('Está pergunta aceita apenas números inteiros.\nTente novamente!')
print('CALCULANDO...')
sleep(1)
print(f'Foram digitados {cont - 1} números.\nE a soma entre eles é {soma}.')
print('OBS: O número 999 não participa da contagem e nem da soma dos números.')