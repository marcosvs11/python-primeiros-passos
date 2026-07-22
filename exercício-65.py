from time import sleep
resp = 's'
cont = 1
resultado = 0
maior = float('-inf')
menor = float('inf')
sep = 30 * '='
tit = 'Análise de Números'.center(30, ' ')
print(sep)
print(tit)
print(sep)
while resp != 'n':
    try:
        n1 = int(input(f'Digita o {cont}° valor: '))
        resultado += n1
        cont += 1
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
        resp = input('Quer continuar adcionando números? (s/n): ').lower().strip()
        if resp != 's':
            print('CALCULANDO...')
            sleep(2)
            break
    except ValueError:
        print('Está pergunta aceita apenas números.\nTente novamente!')
print(sep)
print(f'TOTAL DE NÚMEROS: {cont - 1}.')
print(f'MÉDIA: {resultado / (cont - 1)}.')
print(f'MAIOR NÚMERO DIGITADO: {maior}.')
print(f'MENOR NÚMERO DIGITADO: {menor}.')