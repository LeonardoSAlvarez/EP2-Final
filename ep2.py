import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'imagens')

largura = 500
altura = 500
FPS = 60

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
		self.image = pygame.transform.scale(player_img, (50,30))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = largura/2
		self.rect.bottom = altura - 10
		self.speedx = 0



pygame.init()
tela = pygame.display.set_mode((largura, altura))
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

finally:
	pygame.quit()

