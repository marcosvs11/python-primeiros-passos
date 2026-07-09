# Não aceita números negativos!
try:
    a1 = int(input('Digite o 1°termo: '))
    razao = int(input('Digite a razão: '))
    limite = a1 * (10 - 1) * razao
# Poderia refazer o for e criar esse mecanismo dentro do loop, desse jeito aceitaria os negativos.
    for i in range(a1, limite + razao, razao):
        print(i, end=', ')
    print('...')
    print('Fim dos 10 primeiros termos.')
except ValueError:
    print('Está pergunta aceita apenas números!')
    print('Tente novamente.')