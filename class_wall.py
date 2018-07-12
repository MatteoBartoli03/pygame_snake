import pygame, sys, random
from class_snake import Snake

class wall():
	def __init__(self):
		self.position = [40, 100]
		self.body = []
		for x in range(0, 30):
			self.body.append([(self.position[0]+ (x*10)), 100])

	def check_collision(self):
		for bodyPart in self.body[1:]:
			for partOfBody in snake.body[:]:
				if partOfBody == bodyPart:
					return 1
			return 0

	def Body(self):
		return self.body