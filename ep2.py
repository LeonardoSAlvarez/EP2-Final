import pygame
from os import path
import random
img_dir = path.join(path.dirname(__file__), 'imagens')

WIDTH = 500
HEIGHT = 500
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

gravidade = 3

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(path.join(img_dir,'p1.png')).convert()
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50,50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.prev_x = self.rect.x
        self.prev_y = self.rect.y
        self.jump = False
        
        raio = 25

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


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('EP-2')
clock = pygame.time.Clock()
fundo = pygame.image.load(path.join(img_dir, 'fundo.jpg')).convert()
fundo_rect = fundo.get_rect()

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

platform_group = pygame.sprite.Group()
p = Platform(0, HEIGHT - 10, WIDTH, 10)
platform_group.add(p)
p = Platform(300, HEIGHT - 50, WIDTH-300, 10)
platform_group.add(p)

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
                    player.speedy = -30
                    player.jump = True
                    
#                if event.key == pygame.K_SPACE:
#                    tiro = Tiro(player.rect.centerx, player.rect.top)
#                    all_sprites.add(tiro)

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, platform_group, False, pygame.sprite.collide_rect)
        if hits:
            print('colidiu')
            platform = hits[0]
            player.rect.bottom = platform.rect.top
            player.rect.y = player.prev_y
            player.speedy = 0
            player.jump = False

        tela.fill(BLACK)
        tela.blit(fundo, fundo_rect)
        all_sprites.draw(tela)
        platform_group.draw(tela)
        pygame.display.flip()



finally:
    pygame.quit()
