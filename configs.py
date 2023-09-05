# Configurações inicias
import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game Python")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()
    # cores RGB
preta = (0,0,0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)
    # parêmetros da cobra
tamanho_quadrado = 10
velocidade_cobra = 15