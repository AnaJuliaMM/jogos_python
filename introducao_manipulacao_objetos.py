# Inclue a biblioteca no seu arquivo/programa atual
import pygame


# 1. Preparar o computador
pygame.init()
relogio = pygame.time.Clock()


# 2. Configurar a tela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode(
    (LARGURA, ALTURA)
)
pygame.display.set_caption("Meu primeiro Game")


# 3. Criar objetos
bola = pygame.Rect(
    400, # EIXO X - Posição horizontal
    300, # EIXO Y - Posição na vertical
    20, # Largura
    20  # Altura
)
velocidade_em_x = 5
velocidade_em_y = 5


# 4. Laço de repetição que dá movimento ao jogo:
rodando = True
while rodando:

    # PASSO 1 - Monitorar as interações do usuário (eventos)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # PASSO 2 - Movimentar o objeto
    bola.x = bola.x + velocidade_em_x 
    bola.y = bola.y + velocidade_em_y

    # PASSO 3 - Lidar com a colisão
    if bola.left <= 0 or bola.right >= LARGURA:
        velocidade_em_x = velocidade_em_x * -1

    if bola.top <= 0 or bola.bottom >= ALTURA:
        velocidade_em_y = velocidade_em_y * -1
    
    # PASSO 4 - Atualizar a tela
    tela.fill((30,30,30))
    pygame.draw.ellipse(
        tela,           # Tela
        (255,255,0),    # Cor
        bola            # objeto
    )
    pygame.display.flip()
    relogio.tick(60) # 60FPS

pygame.quit()