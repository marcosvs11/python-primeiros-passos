# Palíndromo é quando uma frase pode ser lida exatamente do mesmo jeito, seja da esquerda para direita quanto da direita para esquerda
sep = 30 * '='
tit = 'Verificador de Palíndromo'.center(30, ' ')
print(sep)
print(tit)
print(sep)
frase = input('Digite uma frase qualquer: ').strip().lower()
separada = frase.split()
junto = ''.join(separada)
inverso = ''
for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
if junto == inverso:
    descisao = 'é palíndromo!'
else:
    descisao = 'não é palíndromo!'
print(f'A frase {junto} ao contrário é {inverso}. Portanto, {descisao}')