from time import sleep
sep = 30 * '='
tit = 'Calculadora IMC'.center(30, ' ')
resp = 's'
while resp != 'n':
    try:
        print(sep)
        print(tit)
        print(sep)
        massa = float(input('Digite a sua massa corporal em kg: '))
        altura = float(input('Digite a sua altura em metros (X.XX): '))
        if altura > 3 or altura < 0:
            print('Por gentileza, seguir as orientações de formatação para informar a altura.')
            continue
        imc = massa / (altura**2)
        if imc < 18.5:
            classif = 'ABAIXO DO PESO'
        elif imc < 25:
            classif = 'PESO NOMRAL (EUTROFIA)'
        elif imc < 30:
            classif = 'SOBREPESO (PRÉ-OBESIDADE)'
        elif imc < 35:
            classif = 'OBESIDADE GRAU I'
        elif imc < 40:
            classif = 'OBESIDADE GRAU II (SEVERA)'
        elif imc >= 40:
            classif = 'OBESIDADE GRAU III (MÓRBIDA)'
        print(f'Você possui {massa}kg de massa corporal e {altura} metros de altura.')
        print('PROCESSANDO...')
        sleep(2)
        print(f'IMC: {imc:.2f}.')
        print(f'Classificação: {classif}.')
        if classif != 'PESO NOMRAL (EUTROFIA)':
            perg_ideal = input('Quer saber o seu peso ideal? (s/n): ').strip().lower()
            if perg_ideal == 's':
                print('PROCESSANDO...')
                sleep(2)
                ideal_min = 18.5 * (altura**2)
                ideal_max = 24.9 * (altura**2)
                print(f'A massa corporal ideal deve ser entre {ideal_min:.1f}kg e {ideal_max:.1f}kg.')
                print('Você consegue, eu acredito!')
        else:
            print('Parabéns! Seu IMC está em perfeitas condições!')
        print('UM MOMENTO...')
        sleep(2)
        resp = input('Quer tentar novamente com outros números? (s/n): ').strip().lower()
        if resp != 's':
            print('Saindo...')
            break
    except ValueError:
        print('Este número aceita apenas números!')
        print('Tente novamente.')