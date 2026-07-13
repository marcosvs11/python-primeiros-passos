tot_idade = 0
idade_velho = 0
mulh_20 = 0
men_velho = ''
for i in range (4):  
    # validação do try/except caso por caso.
    while True:
        try:
            nome = input(f'Digite o nome da {i+1}° pessoa: ').title().strip()
            idade = int(input(f'Digite a idade da {i+1}° pessoa: '))
            sexo = input('Digite o seu sexo (m/f): ').strip().lower()
            print()
            # validação caso o usuário digita incorretamente.
            if sexo != 'm' and sexo != 'f':
                print('Escolha de sexo inválida. Tente novamente!')
                print()
                continue
            # validação caso o usuário digita idade negativa.
            if idade < 0:
                print('Idade inválida. Tente novamente!')
                print()
                continue
            tot_idade += idade
            # 1° desafio: mostrar o nome do HOMEM mais velho.
            if sexo == 'm' and idade > idade_velho:
                idade_velho = idade
                men_velho = nome
            # 2° desafio: mostrar quantas mulheres com 20 anos ou menos.
            if sexo == 'f' and idade <= 20:
                mulh_20 += 1
            break
        except ValueError:
            print('Está pergunta aceita apenas números!')
            print('Tente novamente.')
            print()
            continue
# controle de gramática.
if mulh_20 > 1:
    desc = 'mulheres'
else: 
    desc = 'mulher'
# 3° desafio: média de idade do grupo.
media = tot_idade / 4
print(f'A média de idade entre essas 4 pessoas é de {media:.1f} anos!')
# validação caso não tenha nenhum HOMEM no grupo.
if men_velho == '':
    print('Não foi encontrado um participante HOMEM neste grupo!')
else:
    print(f'O nome do HOMEM mais velho é {men_velho} e ele tem {idade_velho} anos!')
print(f'E nesse grupo, possui {mulh_20} {desc} com 20 anos ou menos!')
