n1 = int(input('Digite um número: '))
n1 = str(n1)
print(f'Unidade: {n1[-1]}')
if len(n1) >= 2:
    print(f'Dezena: {n1[-2]}')
if len(n1) >= 3:
    print(f'Centena: {n1[-3]}')
if len(n1) == 4:
    print(f'Milhar: {n1[-4]}')