import pygame
from os import path
import random
img_dir = path.join(path.dirname(__file__), 'imagens')

WIDTH = 500
HEIGHT = 500
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
		self.image = pygame.transform.scale(player_img, (50,50))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH/2
		self.rect.bottom = HEIGHT - 10
		self.speedx = 0
		raio = 25

	def update(self):
		self.rect.x += self.speedx
		if self.rect.right > WIDTH:
			self.rect.right = WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

class Obstaculos(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		Obstaculos_img = pygame.image.load(path.join(img_dir, 'nuvem1.png')).convert()
		self.image = pygame.transform.scale(Obstaculos_img, (50,50))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedx = random.randrange(-3,3)
		self.speedy = random.randrange(2, 9)
		self.raio = int(self.rect.width* .85/2)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
			self.rect.x = random.randrange(WIDTH - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedx = random.randrange(-3, 3)
			self.speedy = random.randrange(2, 9)

class Tiro(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		tiro_img = pygame.image.load(path.join(img_dir, 'tiros.png')).convert()
		self.image = tiro_img
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10
	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

pygame.init()
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('EP-2')
clock = pygame.time.Clock()
fundo = pygame.image.load(path.join(img_dir, 'fundo.jpg')).convert()
fundo_rect = fundo.get_rect()

player = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

obstaculos = pygame.sprite.Group()
tiro = pygame.sprite.Group()

for i in range(8):
	v = Obstaculos()#nuvem
	all_sprites.add(v)
	obstaculos.add(v)

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

				if event.key == pygame.K_SPACE:
					tiro = Tiro(player.rect.centerx, player.rect.top)
					all_sprites.add(tiro)


			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					player.speedx = 0
				if event.key == pygame.K_RIGHT:
					player.speedx = 0

		all_sprites.update()


		#colisao = pygame.sprite.groupcollide(obstaculos, tiro, True, True)
		#for hit in colisao:
		#	v = Obstaculos()
		#	all_sprites.add(v)
		#	obstaculos.add(v)

		#colisao = pygame.sprite.spritecollide(player, obstaculos, False, pygame.sprite.collide_circle)
		#if colisao:
		#	run = False


		tela.fill(BLACK)
		tela.blit(fundo, fundo_rect)
		all_sprites.draw(tela)
		pygame.display.flip()



finally:
	pygame.quit()
