from random import randint

# Função sorteadora
def sorteia(lista):
    for i in range(5):
        lista.append(randint(1,11))

    print(f'Números sorteados: {lista}.')

# Função soma números pares
def somaPar(lista):
    valoresPares = []
    somadorPares = 0
    print('A soma dos valores pares', end=' ')
    for valor in lista:
        if valor % 2 == 0:
            valoresPares.append(valor)
            somadorPares += valor

    print(f'{valoresPares} igual a {somadorPares}.')

# Programa principal
numeros = []

sorteia(numeros)
somaPar(numeros)
