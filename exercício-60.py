n1 = int(input('Digite um número: '))
resultado = 0
while n1 != 0:
    if n1 - 1 != 0:
        resultado = n1 * (n1 - 1)
    else:
        resultado = n1 * n1
print(f'O {n1}! é igual a {resultado}')