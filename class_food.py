import pygame, sys, random 

class foodSpawner():
	def __init__(self):
		#variabili di base del food
		self.position = [random.randrange(4, 53)*10, random.randrange(4, 53)*10]
		self.isFoodOnTheScreen = True 

	def spawnFood(self):
		#posizionamento food
		#poi naturalmente bisognerà controllare il pos dei muri e del serpente! 
		if self.isFoodOnTheScreen == False:
			self.position = [random.randrange(4, 53)*10, random.randrange(4, 53)*10]
			self.isFoodOnTheScreen = True 
		return self.position

	def setFoodOnScreen(self, b):
		self.isFoodOnTheScreen = b