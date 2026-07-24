from time import sleep
multiplicador = 1
resultado = 0
n1 = 0
sep = 30 * '='
tit = 'Tabuada Vieira'.center(30, ' ')
print(sep)
print(tit)
print(sep)
# Criação de um loop infinito consciente.
while True:
    try:
        n1 = int(input(f'Digite o um número para ver a tabuada (negativo para sair): '))
        # Validação para impedir que a operação ocorra com número negativo.
        if n1 < 0:
            print('Número negativo encontrado!')
            print('Encerrando programa...')
            break
        print('CALCULANDO...')
        sleep(1)
        # Idéia lógica para o cálculo funcionar como tabuada, sem o uso do 'for'.
        while multiplicador != 11:
            resultado = n1 * multiplicador
            print(f'{n1} x {multiplicador} = {resultado}')
            multiplicador += 1
        multiplicador = 1
    except ValueError:
        print('Está pergunta aceita apenas números inteiro!\nTente novamente.')