# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from os import path
import random

# Estabelece a pasta que contem as figuras.
img_dir = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
WIDTH = 480 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # Frames por segundo

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Asteroids")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()

class Player (pygame.sprite.Sprite):
    
    def __init__(self):
        #Construtuor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        
        #Carregando a imagem de fundo
        player_img = pygame.image.load(path.join(img_dir, "playerShip1_orange.png"))
        self.image = player_img
        
        #Diminuindo o tamanho da imagem
        self.imagem = pygame.transform.scale(player_img, (50,38))
        
        #Deixando transparente
        self.image.set_colorkey(BLACK)
        
        #Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()
        
        #Centraliza embaixo da tela
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        
        #Velocidade da nave
        self.speedx = 0
    
    #Metodo que atualiza a posição da nave
    def update (self):
        self.rect.x += self.speedx
        
        #Mantendo ela dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
    
class Mob(pygame.sprite.Sprite):
    
    def __init__(self):
        #Construtuor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)
        #Variável com a imagem
        meteoro_img = pygame.image.load(path.join(img_dir, "meteorBrown_med1.png"))
        self.image = meteoro_img
        
        #Detalhes sobre o posicionamento
        self.rect = self.image.get_rect()
        #Iniciando em uma posição aleatória
        self.rect.x = random.randrange (0, WIDTH)
        self.rect.y = random.randrange (-100, -40)
        
        #Selecionando velocidades aleatorias
        self.speedx = random.randrange (-3,3)
        self.speedy = random.randrange(2,9)
        
    #Metodo que atualiza a posição do meteoro
    def update (self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        

#Cria uma nave. O construtor será chamado automaticamente
player = Player()

#Cria um grupo de sprites e adiciona a nave
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


mob = Mob()
#Grupo de mobs (8 mobs)
for i in range (1,8):
    all_sprites.add(mob) #Adiciona aos sprites


# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
        # Verifica se foi fechado
            if event.type == pygame.QUIT:
                running = False
                
        # Verifica se apertou alguma tecla
            if event.type == pygame.KEYDOWN:
                #Dependendo da tecla, altera a velocidade
                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
        #Verifica se soltou alguma tecla
            if event.type == pygame.KEYUP:
                #Deixa a velocidade 0 novamente
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                
        #Depois de processar os eventos
        #Atualiza a acso de cada sprite 
        all_sprites.update()
    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()
