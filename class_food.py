import pygame, sys, random 

class foodSpawner():
	def __init__(self):
		self.position = [random.randrange(4, 53)*10, random.randrange(4, 53)*10]
		self.isFoodOnTheScreen = True 

	def spawnFood(self):
		if self.isFoodOnTheScreen == False:
			self.position = [random.randrange(4, 53)*10, random.randrange(4, 53)*10]
			self.isFoodOnTheScreen = True 
		return self.position

	def setFoodOnScreen(self, b):
		self.isFoodOnTheScreen = b