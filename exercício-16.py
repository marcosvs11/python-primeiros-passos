import random
sep = 30*'='
tit = 'Quem Vai Limpar o Quadro?'.center(30, ' ')
quant = int(input('Quantos nomes vão participar do sorteio? -> '))
nomes = [''] * quant
resp = 's'
print(sep)
print(tit)
print(sep)
for i in range(quant):
    nomes[i] = input(f'Digite o nome {[i+1]}: ')
print()
print(f'O nome de quem vai limpar o quadro é: {random.choice(nomes).upper()}')
while resp != 'n':
    resp = input('Quer sortear novamente? (s/n): ')
    if resp == 's':
        print(f'O nome de quem vai limpar o quadro é: {random.choice(nomes).upper()}')
print('Saindo...')