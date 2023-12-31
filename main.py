import random

import pygame.draw

from configs import *

def gerar_comida():
    comida_x = round(random.randrange(0,largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0,altura - tamanho_quadrado)/float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x,comida_y,tamanho,tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1],tamanho,tamanho])


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 20)
    texto = fonte.render(f"Pontos: {pontuacao}",True, vermelha)
    tela.blit(texto, [1,1])

def selecionar_deslocamento(tecla):
    if tecla == pygame.K_DOWN:
        deslocamento_x = 0
        deslocamento_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        deslocamento_x = 0
        deslocamento_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        deslocamento_x = tamanho_quadrado
        deslocamento_y = 0
    elif tecla == pygame.K_LEFT:
        deslocamento_x = -tamanho_quadrado
        deslocamento_y = 0
    return deslocamento_x, deslocamento_y

# Loop infinito
def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2
    deslocamento_x = 0
    deslocamento_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x,comida_y = gerar_comida()
    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                deslocamento_x, deslocamento_y = selecionar_deslocamento(evento.key)
    # desenhar os objetos do jogo na tela
        #pontuação
        desenhar_pontuacao(tamanho_cobra - 1)
        # comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)


        # atualizar a posicao da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        x += deslocamento_x
        y += deslocamento_y
        #cobra
        #x e y é a posição atual da cobra
        pixels.append([x,y])
        if len(pixels) > tamanho_cobra:
           #deleta o pixel do "rabo" da cobra
            del pixels[0]
       #checa se a cobra ta batendo nela mesma com exceção da cabeça
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fim_jogo = True

        desenhar_cobra(tamanho_quadrado,pixels)

    # criar a lógica de terminar o jogo
        # cobra bateu na parede
        # cobra bateu nela mesma

    # pegar a interação do usuários
        # fechou a tela
        # apertou as teclas do teclado para mover a cobra
    # Atualização da tela
        pygame.display.update()

    #criar nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comida_x, comida_y = gerar_comida()
        relogio.tick(velocidade_jogo)

rodar_jogo()