import random
resp = 's'
while resp != 'n':
    nomes = ['Marcos', 'Giovanni', 'Annelise', 'Aline', 'João Victor', 'Alan', 'Laryssa']
    print('Sorteador de Nomes'. center(30, ' '))
    enter  = input('Digite "ENTER" para começar: ')
    ale = random.choice(nomes)
    print(f'Você sorteou: {ale}')
    resp = input('Quer sortear o próximo? (s/n): ')
    if resp != 's':
        break