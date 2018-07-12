import pygame, random

class Wall():
	def __init__(self):
		self.body = [[50, 100], [60, 100], [70, 100], [80, 100], [90, 100], [100, 100]]

	def get_body(self):
		return self.body