elenco = []

while True:
    jogador = {}
    gols = []

    # Nome (aceita qualquer non-empty)
    while True:
        nome = input('Digite o nome do jogador: ').strip()
        if nome:
            jogador['nome'] = nome
            break
        print('Nome vazio. Digite um nome válido.')

    # Quantidade de partidas (inteiro >= 0)
    while True:
        try:
            partidas = int(input('Quantidade de partidas jogadas: '))
            if partidas < 0:
                print('Digite um número inteiro não negativo.')
                continue
            break
        except ValueError:
            print('Entrada inválida. Digite um número inteiro.')

    jogador['partidas'] = partidas
    total = 0

    # Gols por partida (cada um inteiro >= 0)
    for i in range(partidas):
        while True:
            try:
                g = int(input(f'Gols marcados na partida {i+1}: '))
                if g < 0:
                    print('Digite um número de gols não negativo.')
                    continue
                gols.append(g)
                total += g
                break
            except ValueError:
                print('Entrada inválida. Digite um número inteiro.')

    jogador['gols'] = gols[:]
    jogador['total'] = total

    elenco.append(jogador.copy())

    resp = input('Quer continuar: (S/N): ').strip().upper()
    if resp != 'S':
        print('CALCULANDO RESULTADOS...')
        break

# Exibição da tabela
print(60 * '-')
print(f"{'código':<7}", end='')
print(f"{'nome':<17}", end='')
print(f"{'gols':<17}", end='')
print(f"{'total':7}")
print(60 * '-')
for c, jogador in enumerate(elenco):
    print(f"{c + 1:^7}{jogador['nome']:<17}{str(jogador['gols']):<17}{jogador['total']:<7}")
print(60 * '-')

# Consulta de estatísticas por jogador
while True:
    entrada = input('Digite o código do jogador (999 para sair): ').strip()
    try:
        codigo = int(entrada)
    except ValueError:
        print('ERRO! Digite um código numérico.')
        continue

    if codigo == 999:
        print('DESLIGANDO...')
        break
    if codigo < 1 or codigo > len(elenco):
        print('ERRO! Digite o código corretamente.')
        continue

    jogador = elenco[codigo - 1]
    print(60 * '-')
    print(f"ESTATÍSTICA DO {jogador['nome'].upper()}".center(60))
    print(60 * '-')
    if not jogador.get('gols'):
        print('Este jogador não disputou partidas.'.center(60))
    else:
        for i, gol in enumerate(jogador['gols']):
            print(f'Na {i + 1}° partida, {gol} gol.'.center(60))
