sep = 30*'='
tit = f'Seu Nome Tem {'Silva?'}'.center(30, ' ')
resp = 's'
while resp != 'n':
    print(sep)
    print(tit)
    print(sep)
    nome = input('Digite o seu nome completo: ')
    sbnome = 'silva'
    if sbnome in nome.lower():
        print(f'Sobrenome {'Silva'} encontrado!')
    else:
        print(f'Não foi possível encontrar o sobrenome {'Silva'}!')
    resp = input('Quer tentar novamento? (s/n): ')
    if resp != 's':
        print('Saindo...')
        break