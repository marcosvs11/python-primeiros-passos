from time import sleep
# Função para mostrar linhas de separação
def mostrarLinha():
    print('-' * 50)

# Função para realizar a contagem
def contador(inicio, fim, passo):
    # Validação do 0
    if passo == 0:
        passo = 1

    # Retirei os possíveis passos negativos
    passo = abs(passo)

    # Ordem crescente/decrescente
    if inicio > fim:
        fim -= 1
        passo = -passo
    else:
        fim += 1

    # Loop para ocorrer a contagem
    print('->', end=' ')
    for i in range(inicio, fim, passo):
        print(i, end='  ')
        sleep(0.1)
    print('ACABOU!')

# Programa principal
mostrarLinha()
print('CONTAGEM DE 1 ATÉ 10 DE 1 EM 1:')
contador(1, 10, 1)
mostrarLinha()
print('CONTAGEM DE 10 ATÉ 0 DE 2 EM 2:')
contador(10, 0, -2)
mostrarLinha()
print('Decida a sua contagem!')
i = int(input('Digite um número para iniciar: '))
f = int(input('Digite um número para terminar: '))
p = int(input('Intervalo: '))
mostrarLinha()
print(f'CONTAGEM DE {i} ATÉ {f} DE {abs(p)} EM {abs(p)}:')
contador(i, f, p)