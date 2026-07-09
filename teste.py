soma = 0
s_pares = []
for i in range(0, 6):
    num = int(input(f'Digite o {i+1}° valor: '))
    if num % 2 == 0:
        soma += num
        s_pares.append(num)
print(f'A soma dos números {(', '.join(map(str, s_pares)))}, que são pares, é igual a {soma}')