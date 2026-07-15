while True:
    sexo = input('Digite o seu sexo (m/f): ').strip().lower()
    if sexo != 'm' and sexo !='f':
        print('Sexo não identificado, tente novamente!')
        continue
    if sexo == 'm':
        escolha = 'masculino'
    elif sexo == 'f':
        escolha = 'feminino'
    print(f'Você é do sexo {escolha}!')
    break