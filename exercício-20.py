import pygame
pygame.mixer.init()
pygame.mixer.music.load('/home/marcosvieira/Projetos/Python/python-primeiros-passos/audioteste.mp3')
pygame.mixer.music.play()
opcao = 1
sep = 30*'='
tit = 'Tocador .MP3'.center(30, ' ') 
while opcao != 0:
    try:
        print(sep)
        print(tit)
        print(sep)
        print('1 - Pausar')
        print('2 - Retomar')
        print('3 - Reniciar')
        print('0 - Sair')
        opcao = int(input('Digite sua opção: '))
        if opcao == 1:
            pygame.mixer.music.pause()
        
        elif opcao == 2:
            pygame.mixer.music.unpause()

        elif opcao == 3:
            pygame.mixer.music.play()
        else:
            print('Saindo...')
            break
    except ValueError:
        print('Este programa aceita apenas números. Tente novamente!')
