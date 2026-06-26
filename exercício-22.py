n1 = input('Digite um número: ')
if n1 < 10:
    print(f'Unidade: {n1}')
elif n1 >= 10:
    print(f'Unidade: {n1[0]}')
    print(f'Dezena: {n1[1]}')
elif n1 >= 100:
    print(f'Unidade: {n1[0]}')
    print(f'Dezena: {n1[1]}')
    print(f'Centena: {n1[2]}')
elif n1 < 9999:
    print(f'Unidade: {n1[0]}')
    print(f'Dezena: {n1[1]}')
    print(f'Centena: {n1[2]}')
    print(f'Milhar: {n1[3]}')


