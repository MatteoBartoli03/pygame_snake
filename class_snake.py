import pygame, random

class Snake():
	def __init__(self):
		#caratteristiche di base dello snake
		self.position = [100,50]
		self.body = [[100, 50],[90,50],[80,50],[70,50],[60,50],[50,50]]
		self.direction = "RIGHT"
		self.changeDirectionTo = self.direction

	def ChangeDirTo(self, dir):
		#cambio di direzione
		if dir == "RIGHT" and not self.direction == "LEFT":
			self.direction = "RIGHT"
		if dir == "LEFT" and not self.direction == "RIGHT":
			self.direction = "LEFT"
		if dir == "UP" and not self.direction == "DOWN":
			self.direction = "UP"
		if dir == "DOWN" and not self.direction == "UP":
			self.direction = "DOWN"

	def move(self, foodPos):
		#movimenti dello snake
		if self.direction == "RIGHT":
			self.position[0] += 10
		if self.direction == "LEFT":
			self.position[0] -= 10
		if self.direction == "UP":
			self.position[1] -= 10
		if self.direction == "DOWN":
			self.position[1] += 10

		#aumento caselle serpente quando snake mangia cibo
		self.body.insert(0, list(self.position))
		
		#controllo snake mangia food
		if self.position == foodPos:
			return 1
		else:
			self.body.pop()
			return 0

	def checkCollision(self):
		#controllo collisione
		if self.position[0] > 530 or self.position[0] < 40:
			return 1

		elif self.position[1] > 530 or self.position[1] < 40:
			return 1

		for bodyPart in self.body[1:]:
			if self.position == bodyPart:
				return 1
		return 0

	def getBody(self):
		return self.body