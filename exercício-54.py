from sys import exit
from time import sleep
cont_menor = 0
cont_maior = 0
for i in range(7):
    while True:
        try:
            idade = int(input(f'Digite a idade da {i+1}° pessoa: '))
            if idade < 18:
                cont_menor += 1
            else:
                cont_maior += 1
            break
        except ValueError:
            print('Está pergunta aceita apenas números!')
            print('Tente novamente.')
print('PROCESSANDO...')
sleep(2)
print(f'Dessas 7 pessoas, {cont_maior} são maiores de idade!')
print(f'E {cont_menor} ainda não atingiram a maioridade!')