# Inclui bibliotecas
import pygame
import random # PARA GERAR NÚMEROS ALEATÓRIOS

# 1. Preparar o computador
pygame.init()
relogio = pygame.time.Clock()
fonte = pygame.font.SysFont("Arial", 50)


# 2. Configurar a tela
LARGURA = 800
ALTURA = 600

tela = pygame.display.set_mode(
    (LARGURA, ALTURA)
)
pygame.display.set_caption("PONG")


# 3. Criar objetos
bola = pygame.Rect(
    400, # Posição EIXO X (horizontal)
    300, # Posição EIXO Y (vertical)
    20, # Largura
    20  # Altura
)
cor_bola = (255,255,0) # RGB
velocidade_bola_x = 9
velocidade_bola_y = 9

jogador = pygame.Rect(
    770, # Posição EIXO X (horizontal)
    250, # Posição EIXO Y (vertical)
    15, # Largura
    100  # Altura
)
cor_jogador = (255,255,255) #RGB
velocidade_jogador_y = 15


# 4. Laço de repetição que dá movimento 
pontos = 0
rodando = True

while rodando:

    # PASSO 1 - Monitorar as interações do usuário
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # PASSO 2 - Movimento do jogador

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_UP] and jogador.top > 0:
        jogador.y = jogador.y - velocidade_jogador_y

    if teclas[pygame.K_DOWN] and jogador.bottom < ALTURA:
        jogador.y = jogador.y + velocidade_jogador_y


    # PASSO 3 - Movimentar a bola
    bola.x = bola.x + velocidade_bola_x
    bola.y = bola.y + velocidade_bola_y


    # PASSO 4 - Lidar com as colisões

    if bola.top <= 0 or bola.bottom >= ALTURA:
        velocidade_bola_y = velocidade_bola_y * -1
    
    if bola.left <= 0:
        velocidade_bola_x = velocidade_bola_x * -1
    
    if bola.right >= LARGURA:
        bola.x = 400
        bola.y = 300
        velocidade_bola_x = velocidade_bola_x * -1
        pontos = 0
    
    if bola.colliderect(jogador):
        velocidade_bola_x = velocidade_bola_x * -1
        pontos = pontos + 1
        cor_bola = (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )


    # PASSO 5 - Mostrar ao usuário
    tela.fill(
        (3,173,252)
    )

    texto_pontos = fonte.render(
        f"Pontos: {pontos}",
        True,
        (255,255,255)
    )
    tela.blit(
        texto_pontos, # Mensagem 
        (50,50) # Posição
    )

    pygame.draw.ellipse(
        tela,
        cor_bola,
        bola
    )
    pygame.draw.rect(
        tela,
        cor_jogador,
        jogador
    )

    pygame.display.flip()
    relogio.tick(60) # 60 FTS

pygame.quit()