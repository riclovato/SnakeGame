from configs import *
# Loop infinito
def rodar_jogo():
    fim_jogo = False

    while not fim_jogo:
        tela.fill(preta)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
    # desenhar os objetos do jogo na tela
        #pontuação
        #cobra
        #comida

    # criar a lógica de terminar o jogo
        # cobra bateu na parede
        # cobra bateu nela mesma

    # pegar a interação do usuários
        # fechou a tela
        # apertou as teclas do teclado para mover a cobra


rodar_jogo()