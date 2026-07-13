# referência para que a 1° tentativa aconteça.
peso_maior = 0
# mesma situação, mas nesse caso precisa de um positivo infinito.
peso_menor = float('inf')
for i in range(5):
    peso = float(input(f'Digite a peso da {i + 1}° pessoa: '))
    if peso > peso_maior:
        peso_maior = peso
# dois if independentes para não ter interferência.
    if peso < peso_menor:
        peso_menor = peso
print(f'Maior peso lido: {peso_maior:.2f}KG.')
print(f'Menor peso lido: {peso_menor:.2f}KG.')