life = 3
speed = 10
score = 0


while True:
	import pygame, sys, random, time
	from class_snake import Snake
	from class_food import foodSpawner
	from pygame.locals import *
	from time import gmtime, strftime
	pygame.init()
	while True:
		screen = pygame.display.set_mode((580, 580))
		bg = pygame.image.load('prato_bg.jpg')
		ICON = pygame.image.load('ICON.png')	
		pygame.display.set_icon(ICON)

		pygame.display.set_caption("Snake game by Francesco & Matteo")
		fps = pygame.time.Clock()

		snake = Snake()
		foodSpawner = foodSpawner()

		def gameOver():
			pygame.quit()
			sys.exit()

		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						snake.ChangeDirTo("RIGHT")
					if event.key == pygame.K_LEFT:
						snake.ChangeDirTo("LEFT")
					if event.key == pygame.K_UP:
						snake.ChangeDirTo("UP")
					if event.key == pygame.K_DOWN:
						snake.ChangeDirTo("DOWN")

			foodPos = foodSpawner.spawnFood()
			if snake.move(foodPos) == 1:
				score += 1
				foodSpawner.setFoodOnScreen(False)

			if score == 5:
				speed = 12.5
			if score == 10:
				speed = 15
			if score == 2:
				position_of_wall = [40, 100]
				body_of_wall = []
				for x in range(0, 30):
					body_of_wall.append([(position_of_wall[0]+ (x*10)), 100])
					body_of_wall.append([(position_of_wall[0]+ (x*10)), 110])

			screen.blit(bg, [0, 0])

			for pos in snake.getBody():
				pygame.draw.rect(screen, pygame.Color(225,218,228), pygame.Rect(pos[0], pos[1], 10, 10))

			if score >= 2:
				for pos in body_of_wall:
					pygame.draw.rect(screen, pygame.Color(53,53,53), pygame.Rect(pos[0], pos[1], 10, 10))

			pygame.draw.rect(screen, pygame.Color(231,0,0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))


			a=0
			if score >= 2:
				for bodyPart in body_of_wall[1:]:
					for partOfBody in snake.body[:]:
						if partOfBody == bodyPart:
							a = 1
							break

			if snake.checkCollision() == 1 or a == 1:
				life -= 1
				break

			if life == 0:
				bg = pygame.image.load('prato_bg.jpg')
				font = pygame.font.SysFont("Comfortaa", 100)
				surf_text = font.render("GAME OVER...", True, (0, 0, 0))
				screen.blit(surf_text, (60, 250))                            
				pygame.display.flip()
				done = False
				while not done:
					for ev in pygame.event.get():
							if ev.type == QUIT:
								done = True
					pygame.quit()
					sys.exit()

		#	LIFE_SCORE = "LIFE: " + str(life) + "   SCORE: " + str(score)
		#	bg = pygame.image.load('prato_bg.jpg')
		#	font = pygame.font.SysFont("Comfortaa", 30)
		#	surf_text = font.render(LIFE_SCORE, True, (255, 255, 255))
		#	screen.blit(surf_text, (10, 10))                            
		#	pygame.display.flip()
		#	done = False
		#	while True:
		#		for ev in pygame.event.get():
		#				if ev.type == QUIT:
		#					break
		#		break

			#bg = pygame.image.load('prato_bg.jpg')
			#font = pygame.font.SysFont("Comfortaa", 20)
			#surf_text = font.render('SNAKE            FOOD            WALL', True, (255, 255, 255))
			#screen.blit(surf_text, (120, 555))                            
			#pygame.display.flip()
			#done = False
			#while True:
			#	for ev in pygame.event.get():
			#			if ev.type == QUIT:
			#				break
			#	break
			
			pygame.display.flip()
			fps.tick(speed)


		if snake.checkCollision() == 1 or a == 1:
			break