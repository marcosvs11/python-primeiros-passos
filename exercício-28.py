resp = 's'
sep = 40*'='
tit = 'Radar de Velocidade - Rodovia'.center(40, ' ')
lim = 80
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        vel = int(input('Digite a velocidade: '))
        if vel > lim:
            velUt = vel - lim
            mul = 7 * velUt 
            print('Você foi multado!')
            print(f'O limite permitido nesta via é de {lim} Km/h e você passou em {vel} Km/h!')
            print(f'O valor devido é de: R$ {mul:,.2f}')
            print('OBS: R$ 7,00 por KM excedente.')
        else:
            print('Liberado para seguir viagem, velocidade dentro da normalidade.')
            print(f'O limte permitido nesta via é de {lim} km/h e você passou em {vel} km/h!')
        resp = input('Quer tentar com uma velocidade diferente? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas números!')
        print('Tente novamente.')