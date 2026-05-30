print('============================')
print('  Calculadora do Marcos')
print('============================')

opcao = 1
while (opcao != 0):
    print('1 - Somar')
    print('2 - Subtrair')
    print('3 - Multiplicar')
    print('4 - Dividir')
    print('0 - Sair')
    opcao = int(input('Escolha uma opção: '))

    if(opcao != 0):
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    
    if(opcao == 1):
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
    
    elif(opcao == 2):
        subtra = n1 - n2
        print(f'{n1} + {n2} = {subtra}')

    elif(opcao == 3):
        multi = n1 * n2
        print(f'{n1} + {n2} = {multi}')

    elif(opcao == 4):
        if(n1 == 0):
            print('Impossível zero ser divisível, tente novamente!')
        else:
            divi = n1 / n2
            print(f'{n1} / {n2} = {divi}')

print('Saindo...')