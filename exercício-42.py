from time import sleep
sep = 30 * '='
tit = 'Formador de Triângulos'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        la = int(input('Digite o comprimento do lado A (cm): '))
        lb = int(input('Digite o comprimento do lado B (cm): '))
        lc = int(input('Digite o comprimento do lado C (cm): '))
        print('PROCESSANDO...')
        sleep(2)
        if la + lb > lc and la + lc > lb and lb + lc > la:
            condição = 'VERDADEIRO'
            veredito = ''
        else:
            condição = 'FALSO'
            veredito = 'NÃO'
        print(f'{condição}: O lado A com {la}cm, lado B com {lb}cm e o lado C com {lc}cm {veredito} podem formar um triângulo!')
        if condição == 'VERDADEIRO':
            if la == lb == lc:
                classif = 'EQUILÁTERO'
                caract = 'TODOS OS LADOS POSSUEM A MESMA MEDIDA'
            elif la == lb or lb == lc or lc == la:
                classif = 'ISÓSCELES'
                caract = 'DOIS LADOS POSSUEM A MESMA MEDIDA'
            elif la != lb != lc:
                classif = 'ESCALENO'
                caract = 'TODOS OS LADOS POSSUEM MEDIDAS DIFERENTES'
            print(f'OBSERVAÇÃO: Este triângulo é {classif}, pois {caract}!')
        resp = input('Quer tentar novamente com outras medidas? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números! Tente novamente.')