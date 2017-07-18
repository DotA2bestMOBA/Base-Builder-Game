import pygame
from pygame.locals import *
import math


pygame.init()

screen = pygame.display.set_mode((1400,900), 0, 32)
WHITE = (255, 255, 255)
blue = (75, 175, 255)
screen.fill(blue)
alpha = 128
picture = pygame.image.load('/Users/sundar/Desktop/island.png')
island = pygame.transform.scale(picture, (350, 300))
MAX_HP = 1000
MAX_POWER = 10000

#clock = pygame.time.Clock()
def draw_grid(): #draws the demo grid for the players to use to place blocks
	for i in range(5): # for each time the i is within the height
		for j in range(10): # for each time j is within the width

			#demo hp and power to test the health and power bars
			hp = 800 
			power = 5000

			#these draw the squares on the grid to show the player where they are allowed to place the blocks
			pygame.draw.rect(screen, (211, 211, 209), (10 + 35 * j, 375 + 35 * i, 35, 35))
			pygame.draw.rect(screen, (0, 0, 0), (10 + 35 * j, 375 + 35 * i, 35, 35), 2)
			pygame.draw.rect(screen, (211, 211, 209), (1040 + 35 * j, 375 + 35 * i, 35, 35))
			pygame.draw.rect(screen, (0, 0, 0), (1040 + 35 * j, 375 + 35 * i, 35, 35), 2)

			#sents the font and the text that will display the amount of power and health the player has
			font = pygame.font.SysFont("comicsansms", 30)
			text_hp = font.render("HP: " + str(hp) + " / " + str(MAX_HP), True, (0, 128, 0))
			text_power = font.render("Power: " + str(power) + " / " + str(MAX_POWER), True, (0,128,0))

			#draws the health bars and their overlapping self to show a rough percentage of what the player has left
			pygame.draw.rect(screen, (255, 0, 0), (10, 10, 300, 15))
			pygame.draw.rect(screen, (0, 255, 0), (10, 10, hp * 300 / MAX_HP, 15))
			pygame.draw.rect(screen, (255, 0, 0), (1080, 10, 300, 15))
			pygame.draw.rect(screen, (0, 255, 0), (1080, 10, hp * 300 / MAX_HP, 15))

			#This shows the player the power they have to fire the weapons and what the max power is
			pygame.draw.rect(screen, (255, 251, 56), (10, 50, power * 300 / MAX_POWER, 15))	
			pygame.draw.rect(screen, (255, 251, 56), (1080, 50, power * 300 / MAX_POWER, 15))

	#this draws all of the islands and the health bars and power bars with the text to support them
	screen.blit(island, (10, 550))
	screen.blit(island, (1040, 550))
	screen.blit(text_hp, (170, 35))
	screen.blit(text_hp, (1240, 35))
	screen.blit(text_power, (112, 75))
	screen.blit(text_power, (1182, 75))


running = True
#loop to keep our game running
while running: 
	draw_grid()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	pygame.display.update()

