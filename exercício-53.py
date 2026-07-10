# Palíndromo é quando uma frase pode ser lida exatamente do mesmo jeito, seja da esquerda para direita quanto da direita para esquerda
frase = input('Digite uma frase qualquer: ').strip().lower().replace(' ', '')
f_invertida = frase.rfind(frase)
if frase == f_invertida:
    print('PALÍDROMO')
else:
    print('FALSO')