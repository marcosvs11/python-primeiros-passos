# Função com mensagem adaptável
def escreva(msg):
    largura = len(msg) + 6
    print(largura * '-')
    print(msg.center(len(msg) + 6))
    print(largura * '-')


# Programa principal
frase = str(input('Digite uma frase: ')).strip()
escreva(frase)