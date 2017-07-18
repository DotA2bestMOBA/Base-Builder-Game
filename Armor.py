import pygame
from pygame.locals import *
import math

#superclass for armor
class Armor_Sprite(pygame.sprite.Sprite):

	def __init__(self, hp, cost, locationx, locationy, material):
		self.hp = hp
		self.cost = cost
		self.locationx = locationx
		self.locationy = locationy
		self.material = material

	def draw():
		#draws the blocks

	def update():
		#this will detect whether the blocks are hit

#subclass of Armor last-tier armor
class Wood(Armor_Sprite):

	def __init__(self, ):
		#call the arguements that you don't define in this function
		#defind local varibales that are unique to this class  hp values, cost, etc.
		super(Wood, self).__init__()
	#call the functions in the while loop that you are going to use

#subclass of Armor middle-tier armor
class Bronze(Armor_Sprite):

	def __init__(self, ):
		#call the arguements that you don't define in this function
		#defind local varibales that are unique to this class  hp values, cost, etc.
		super(Bronze, self).__init__()
	#call the functions in the while loop that you are going to use

#subclass of Armor best-tier
class Steel(Armor_Sprite):

	def __init__(self, ):
		#call the arguements that you don't define in this function
		#defind local varibales that are unique to this class  hp values, cost, etc.
		super(Steel, self).__init__()
	#call the functions in the while loop that you are going to use