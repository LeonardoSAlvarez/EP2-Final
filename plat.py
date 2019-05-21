#cenarios isometricos
import pygame
from os import path
from pygame.locals import *
WIDTH = 500
HEIGHT = 500
img_dir = path.join(path.dirname(__file__), 'imagens')
FPS = 60
#eixo_x e eixo_y

#imagem do player
player = pygame.image.load('./imagens/p1.png')
#teclas
keys = (False, False, False, False)
player_pos = [200, 100]
velocidade = 0.2
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(path.join(img_dir,'p1.png')).convert()
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.bottom = 250
        self.speedx = 0
        self.speedy = 0
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        self.jump = False
        


    def update(self):
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.jump:
            self.speedy += gravidade
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
player = Player()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)




try:

    run = True
    while run:
        clock.tick(FPS)
        #pygame.display.flip()
        screen.fill(BLACK) #preenchre tela
        #desenha retangulo na tela, padrao RGB, ponto1, ponto2..., preenchimeto
        pygame.draw.polygon(screen, (0, 255, 0), ((10, 250), (250, 110), (500, 250), (250, 390), (10, 250)), 0)
        #desenhar linhas
        pygame.draw.line(screen, (170, 150,0), (9, 270), (250, 410), 42)
        pygame.draw.line(screen, (100, 88, 0), (250, 410), (499, 270), 42)
        casa = pygame.image.load('./imagens/nuvem.png')
        screen.blit(casa, (80, 150)) #imprimimr em cima do losago
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    player.speedy = -8
                    
                if event.key == pygame.K_LEFT:
                    player.speedx = -8

                if event.key == pygame.K_DOWN:
                    player.speedy = 8

                if event.key == pygame.K_RIGHT:
                    player.speedx = 8

            if event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    player.speedx = 0

                if event.key == pygame.K_LEFT:
                    player.speedx = 0

                if event.key == pygame.K_DOWN:
                    player.speedx = 0

                if event.key == pygame.K_RIGHT:
                    player.speedx = 0


        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

            
finally:
    pygame.quit()