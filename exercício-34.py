sep = 30 * '='
tit = 'Formaria um Triângulo?'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        la = int(input('Digite o comprimento do lado A (cm): '))
        lb = int(input('Digite o comprimento do lado B (cm): '))
        lc = int(input('Digite o comprimento do lado C (cm): '))
        if la + lb > lc and la + lc > lb and lb + lc > la:
            print(f'VERDADEIRO: As retas {la}cm, {lb}cm e {lc}cm podem formar um triângulo!')
        else:
            print(f'FALSO: As retas {la}cm, {lb}cm e {lc}cm NÃO podem formar um triângulo!')
        resp = input('Quer tentar novamente com outras medidas? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números! Tente novamente.')