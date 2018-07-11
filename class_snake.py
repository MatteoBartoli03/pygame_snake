import pygame, random

class Snake():
	def __init__(self):
		self.position = [100,50]
		self.body = [[100, 50],[90,50],[80,50],[70,50],[60,50],[50,50]]
		self.direction = "RIGHT"
		self.changeDirectionTo = self.direction

	def ChangeDirTo(self, dir):
		if dir == "RIGHT" and not self.direction == "LEFT":
			self.direction = "RIGHT"
		if dir == "LEFT" and not self.direction == "RIGHT":
			self.direction = "LEFT"
		if dir == "UP" and not self.direction == "DOWN":
			self.direction = "UP"
		if dir == "DOWN" and not self.direction == "UP":
			self.direction = "DOWN"

	def move(self, foodPos):
		if self.direction == "RIGHT":
			self.position[0] += 10
		if self.direction == "LEFT":
			self.position[0] -= 10
		if self.direction == "UP":
			self.position[1] -= 10
		if self.direction == "DOWN":
			self.position[1] += 10

		self.body.insert(0, list(self.position))
		if self.position == foodPos:
			return 1
		else:
			self.body.pop()
			return 0

	def checkCollision(self):
		if self.position[0] > 490 or self.position[0] < 0:
			return 1

		elif self.position[1] > 490 or self.position[1] < 0:
			return 1

		for bodyPart in self.body[1:]:
			if self.position == bodyPart:
				return 1
		return 0

	def getHeadPosition(self):
		return self.position 

	def getBody(self):
		return self.body