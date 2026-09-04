from datetime import datetime

def voto(nasc):
    # Variável local, mesmo nome da global, mas permite que a função funcione de forma independente.
    anoAtual = datetime.now().year
    idade = anoAtual - nasc
    if idade < 16:
        condicao = f'{idade} anos: VOTO NEGADO!'
    elif idade < 18 or idade > 65:
        condicao = f'{idade} anos: VOTO OPCIONAL!'
    else:
        condicao = f'{idade} anos: VOTO OBRIGATÓRIO!'

    return condicao

# Programa principal
anoAtual = datetime.now().year

while True:
    try:
        anoNasc = int(input('Digite o ano de nascimento (XXXX): '))
        if len(str(anoNasc)) != 4 or anoNasc > anoAtual:
            print('Entrada inválida, digite conforme a indicação!')
            continue
        break
    except ValueError:
        print('Entrada inválida, digite somente números conforme a indicação!')

cond = voto(anoNasc)

print(f'Com a sua idade de {cond}')
