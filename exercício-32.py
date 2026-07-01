sep = 30 * '='
tit = 'Mostre-me o Maior e o Menor'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        n1 = int(input('Digite o 1° número: '))
        n2 = int(input('Digite o 2° número: '))
        n3 = int(input('Digite o 3° número: '))
        menor = min(n1, n2, n3)
        maior = max(n1, n2, n3)
        print(f'O menor número digitado é: {menor}.')
        print(f'E o maior digitado é: {maior}.')
        resp = input('Quer tentar novamente com outros números? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números! Tente novamente')