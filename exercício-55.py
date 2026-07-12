peso_maior = 0
peso_menor = 0
troca = 0
for i in range(5):
    peso = float(input(f'Digite a peso da {i + 1}° pessoa: '))
    if peso > peso_maior:
        peso_maior = peso
    elif peso < peso_menor:
        peso_menor = peso
    else: 
        peso_menor = peso

print(f'MAIOR: {peso_maior:.2f}')
print(f'MENOR: {peso_menor:.2f}')
