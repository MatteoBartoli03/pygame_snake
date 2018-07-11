life = 3

while True:
	import pygame, sys, random, time
	from class_snake import Snake
	from class_food import foodSpawner
	from pygame.locals import *
	pygame.init()
	while True:
		screen = pygame.display.set_mode((500, 500))
		bg = pygame.image.load('prato_bg.jpg')
		mela = pygame.image.load('mela.jpg')
		pygame.display.set_icon(mela)

		#pygame.display.set_caption("Snake game by Francesco & Matteo")
		fps = pygame.time.Clock()

		score = 0

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

			screen.blit(bg, [0, 0])
			for pos in snake.getBody():
				pygame.draw.rect(screen, pygame.Color(225,218,228), pygame.Rect(pos[0], pos[1], 10, 10))
			pygame.draw.rect(screen, pygame.Color(231,0,0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

			if snake.checkCollision() == 1:
				life -= 1
				break

			if life == 0:
				bg = pygame.image.load('prato_bg.jpg')
				font = pygame.font.SysFont("Comfortaa", 100)
				surf_text = font.render("GAME OVER...", True, (0, 0, 0))
				screen.blit(surf_text, (15, 200))                            
				pygame.display.flip()
				done = False
				while not done:
					for ev in pygame.event.get():
							if ev.type == QUIT:
								done = True
					pygame.quit()
			if life == -1:
				gameOver()

			LIFE_SCORE = "LIFE: " + str(life) + "   SCORE: " + str(score)
			pygame.display.set_caption(LIFE_SCORE)
			pygame.display.flip()
			fps.tick(7.5)

			if score == 20:
				bg = pygame.image.load('prato_bg.jpg')
				font = pygame.font.SysFont("Comfortaa", 100)
				surf_text = font.render("LEVEL 2", True, (0, 0, 0))
				screen.blit(surf_text, (15, 200))                            
				pygame.display.flip()
				done = False
				while not done:
					for ev in pygame.event.get():
							if ev.type == QUIT:
								done = True
					pygame.quit()

		if snake.checkCollision() == 1:
			break