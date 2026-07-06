from time import sleep
sep = 40 * '='
tit = 'Alistamento Serviço Militar'.center(40, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        idade = int(input('Digite a sua idade: '))
        idminima = 18
        print('PROCESSANDO...')
        sleep(2)
        if idminima == idade:
            print('Você está sendo convocado para o serviço militar obrigatório!')
            print('Não deixe para a última hora, alista-se o quanto antes!')
        elif idminima - idade == 1:
            aniv = input('Você faz aniversário este ano ainda? (s/n): ').strip().lower()
            print('PROCESSANDO...')
            sleep(2)
            if aniv == 's':
                print('Você está sendo convocado para o serviço militar obrigatório!')
            else:
                print('No próximo ano, você sera obrigado a se alistar para o serviço militar!')
        elif idminima - idade == 2:
            aniv = input('Você faz aniversário este ano ainda? (s/n): ').strip().lower()
            print('PROCESSANDO...')
            sleep(2)
            if aniv == 's':
                print('No próximo ano, você sera obrigado a se alistar no serviço militar!')
            else:
                print('Você ainda precisará de 2 anos para o serviço militar obrigatório!')
        elif idminima > idade:
            dif = idminima - idade
            print(f'Você ainda precisará de {dif} anos para o serviço militar obrigatório!')
        elif idade - idminima == 1:
            aniv = input('Você faz aniversário este ano ainda? (s/n): ').strip().lower()
            print('PROCESSANDO...')
            sleep(2)
            if aniv == 's':
                print('Voce deveria ter se alistado a 2 anos atrás!')
            else:
                print('Você deveria ter se alistado no ano passado!')
        elif idade - idminima == 2:
            aniv = input('Você faz aniversário este ano ainda? (s/n): ').strip().lower()
            print('PROCESSANDO...')
            sleep(2)
            if aniv == 's':
                print('Você deveria ter se alistado a 3 anos atrás!')
            else:
                print('Você deveria ter se alistado a 2 anos atrás!') 
        elif idade > idminima:
            dif = idade - idminima
            print(f'Você deveria ter se alistado a {dif} anos atrás')
        sleep(2)
        resp = input('Você quer refazer o cálculo? (s/n): ').lower().strip()
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Está pergunta aceita apenas números!')
        print('Tente novamente.')