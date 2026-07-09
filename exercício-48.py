soma = 0
for i in range(3, 500, 3):
    if i % 2 == 1:
        soma = soma + i
print(f'A soma dos números múltiplos de 3 e ímpares, entre 1 e 500, é igual a {soma}')
print('Acabou...')