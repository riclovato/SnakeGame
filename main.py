import random

from configs import *

def gerar_comida():
    comida_x = round(random.randrange(0,largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0,altura - tamanho_quadrado)/20.0) * 20.0
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x,comida_y,tamanho,tamanho])


# Loop infinito
def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2
    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x,comida_y = gerar_comida()
    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
    # desenhar os objetos do jogo na tela
        #pontuação
        #cobra
        #comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)


    # criar a lógica de terminar o jogo
        # cobra bateu na parede
        # cobra bateu nela mesma

    # pegar a interação do usuários
        # fechou a tela
        # apertou as teclas do teclado para mover a cobra
    # Atualização da tela
        pygame.display.update()
        relogio.tick(velocidade_jogo)

rodar_jogo()