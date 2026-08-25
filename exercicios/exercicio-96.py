# Função para calcular a área
def area(larg, comp):
    valorArea = larg * comp
    print(f'Um terreno com a largura de {larg}m e o comprimento de {comp}m, resulta em uma área de {valorArea:.2f}m².')


# Programa principal
while True:
    print(30 * '-')
    print('Área do Terreno'.center(30))
    print(30 *  '-')
    # Tratamento de erro
    try:
        largura = float(input('Valor da LARGURA (metros): '))
        # Entrada inválida
        if largura <= 0:
            print('Entrada inválida. Por gentileza, adicione um número positivo maior que zero!')
            continue
        else:
            while True:
                # Tratamento de erro + progressão
                try:
                    comprimento = float(input('Valor do COMPRIMENTO (metros): '))
                    # Entrada inválida com volta para a pergunta atual
                    if comprimento <= 0:
                        print('Entrada inválida. Por gentileza, adicione um número positivo maior que zero!')
                        continue
                    # Chamda da função + saída
                    else:
                        area(largura, comprimento)
                        break
                except ValueError:
                    print('Entrada inválida. Por gentileza, adicione apenas números!')
                    continue
    except ValueError:
        print('Entrada inválida. Por gentileza, adicione apenas números!')
        continue
    # Opção para interromper
    resp = input('Quer continuar? (S/N): ').strip().upper()
    if resp != 'S':
        print('Desligando...')
        break