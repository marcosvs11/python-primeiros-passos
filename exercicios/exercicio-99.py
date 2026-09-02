# Lista para receber vários números do usuário
n = []

# Função determinante do maior número
def maior(*num):
    maiorValor = num[0]
    for valor in num:
        if valor > maiorValor:
            maiorValor = valor
    print(maiorValor)

# Programa principal
while True:
    while True:
        try:
            v = int(input('Digite um número: '))
        except ValueError:
            print('Entrada inválida, tente novamente!')
            continue
        break
    n.append(v)
    resp = str(input('Quer continuar (S/N):' )).strip().upper()
    if resp in 'SN':
        if resp == 'S':
            continue
        else:
            print(50 * '-')
            print('GERANDO RESULTADO...')
            break
    else:
        print('Entrada inválida. Por gentileza, digite apenas "S" ou "N"!')
        continue
print('O maior valor dos números digitados: ', end='')
maior(*n)
