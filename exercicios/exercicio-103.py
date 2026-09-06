# Caso a função seja chamada, mas sem os parâmetros.
def ficha(nome = 'não informado', gols = 0):
    # Simulando quando usuário aperta apenas ENTER.
    if nome == '':
        nome = '<não informado>'
    if str(gols).isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} marcou {gols} gol(s)!')

# Programa principal
n = str(input('Digite o nome do JOGADOR: ')).strip().title()
g = str(input('Quantidade de gols marcados: ')).strip()
ficha(n, g)
