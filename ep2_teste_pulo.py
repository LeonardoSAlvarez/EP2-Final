import pygame
from os import path
import random
img_dir = path.join(path.dirname(__file__), 'imagens')

WIDTH = 500
HEIGHT = 500
FPS = 90

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
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT/2
        #self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        raio = 25

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
#como fazer o sprite ficar dentro da tela no eixo y???


pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('EP-2')
clock = pygame.time.Clock()
fundo = pygame.image.load(path.join(img_dir, 'fundo.jpg')).convert()
fundo_rect = fundo.get_rect()

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

try:
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speedx = -8

                if event.key == pygame.K_RIGHT:
                    player.speedx = 8

                if event.key == pygame.K_UP:
                    player.speedy = -8

                if event.key == pygame.K_DOWN:
                    player.speedy = 8

                if event.key == pygame.K_SPACE:
                    player.speedy = -8
#como fazer o sprite pular                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                if event.key == pygame.K_UP:
                    player.speedy = 0
                if event.key == pygame.K_DOWN:
                    player.speedy = 0
                if event.key == pygame.K_SPACE:
                    player.speedy = 0

        all_sprites.update()
        tela.fill(BLACK)
        tela.blit(fundo, fundo_rect)
        all_sprites.draw(tela)
        pygame.display.flip()



finally:
    pygame.quit()
