from time import sleep
sep = 30 * '='
tit = 'Qual o Fatorial?'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        n1 = int(input('Digite um número: '))
        print('PROCESSANDO...')
        sleep(2)
        # Se o usuário digitar número negatico.
        if n1 < 0:
            print('Número indeterminado. Tente novamente!')
            continue
        resultado = 1
        # Criação de uma variável com o mesmo valor do n1, já que irei mudar o valor no while.
        origem = n1
        # Cálculo do fatorial.
        while n1 > 0:
            resultado *= n1
            n1 -= 1
        print(f'{origem}! = ', end='')
        # For para mostrar os números que estão sendo multiplicados.
        for i in range(origem, 0, -1):
            # Para tirar o 'x' do último número.
            if i == 1:
                print(f'{i}', end='')
            else:
                print(f'{i}x', end='')
        print(f' = {resultado}')
        # Explicação do porquê o 0! é igual a 1.
        if origem == 0:
            print(f'💡 -> O resultado de {n1}! é 1, pois é a única forma de separar 1 objeto!')
        sleep(1)
        resp = input('Quer tentar novamente com outro número? (s/n): ').strip().lower()
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números inteiros!')
        print('Tente novamente.')