from time import sleep
resp = 's'
cont = 1
resultado = 0
# Número infinito negativo, certifica-se que o primeiro número seja o maior.
maior = float('-inf')
# Mesma casa, mas agora positivo, certificando que o primeiro número seja o menor.
menor = float('inf')
sep = 30 * '='
tit = 'Análise de Números'.center(30, ' ')
print(sep)
print(tit)
print(sep)
# Condição para continuar adicionando números.
while resp != 'n':
    try:
        n1 = int(input(f'Digita o {cont}° valor: '))
        # Para mostrar o resultado.
        resultado += n1
        # Contador para o usuário ter noção dos números adicionados.
        cont += 1
        # Certifica se o próximo número é maior que o anterior.
        if n1 > maior:
            maior = n1
        # Certifica se o próximo número é menor que o anterior.
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