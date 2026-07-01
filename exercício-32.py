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
        menor = n1
        if n2 < n1 and n2 < n3:
            menor = n2
        if n3 < n1 and n3 < n2:
            menor = n3
        maior = n1
        if n2 > n1 and n2 > n3:
            maior = n2
        if n3 > n1 and n3 > n2:
            maior = n3
        print(f'O menor número digitado é: {menor}.')
        print(f'E o maior digitado é: {maior}.')
        resp = input('Quer tentar novamente com outros números? (s/n): ').strip()
        if resp.lower() != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números! Tente novamente')