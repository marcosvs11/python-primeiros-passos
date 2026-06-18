import random
quant = int(input('Quantos nomes vai precisar para sortear? -> '))
nomes = [""] * quant

for i in range(quant):
    nomes[i] = input('Digite o nome para o sorteio: ')

print(f'Você sorteou o: {random.choice(nomes).upper()}')