def fatorial(numero, show=False):
    if numero == 0:
        fat = 1
        return fat

    if numero < 0:
        fat = 'Não existe fatorial de número negativo!'
        return fat

    parametro = numero
    fat = 1

    while numero != 0:
        fat *= numero
        if show:
            if numero - 1 == 0:
                print(f'{numero} = ', end='')
            else:
                print(f'{numero} x', end=' ')

        numero -= 1

    return fat

# Programa principal
mostrar = False
while True:
    try:
        num = int(input('Digite um número: '))
    except ValueError:
        print('Entrada inválida, digite apenas números inteiros!')
        continue

    break

resp = str(input('Quer visualizar as operações? (S/N): ')).strip().upper()
mostrar = resp == 'S'

resultado = fatorial(num, mostrar)

print(f'{num}! = {resultado}')
