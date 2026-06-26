sep = 30*'='
tit = f'Sua Cidade Comeca Com {'Santo?'}'
resp = 's'
while resp != 'n':
    print(sep)
    print(tit)
    print(sep)
    cid = input('Qual é a sua cidade? -> ')
    verific = cid.upper().startswith('SANTO')
    if verific == True:
        print(f'Sua cidade realmente começa com {'Santo'}!')
    else:
        print(f'Sua cidade não começa com {'Santo'}, mas sim com {cid.upper().split()[0]}')
    resp = input('Quer tentar novamento? (s/n): ')
    if resp != 's':
        print('Saindo...')
        break