try: 
    print(f'{'='*30} \n   Antecessor e Sucessor \n{'='*30}')
    na = int(input('Digite um número: '))
    print(f'O antecessor de {na} é {na - 1} e o sucessor é {na + 1} ')

except ValueError:
    print('ERRO! Este programa aceita apenas números inteiros. Tente novamente!')