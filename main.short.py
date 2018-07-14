import pygame, sys, random, time
from class_snake import Snake
from pygame.locals import *
from time import gmtime, strftime

#variabili di base
life = 3
speed = 10
score = 0

#impostazione finestra
screen = pygame.display.set_mode((580, 580))
bg = pygame.image.load('prato_bg.jpg')
ICON = pygame.image.load('ICON.png')	
pygame.display.set_icon(ICON)

while True:
	from class_food import foodSpawner

	#inizializzazione di pygame
	pygame.init()

	while True:

		pygame.display.set_caption("Snake game by Francesco & Matteo")
		fps = pygame.time.Clock()

		#assegnamento variabili importate da class_food e class_snake
		snake = Snake()
		foodSpawner = foodSpawner()

		#definiamo la funzione GAME OVER
		def gameOver():
			pygame.quit()
			sys.exit()

		while True:
			#cambi di direzione e spostamenti
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

			#posizionamento cibo
			foodPos = foodSpawner.spawnFood()
			if score == 29:
				foodPos= [270, 270]
			if snake.move(foodPos) == 1:
				score += 1
				foodSpawner.setFoodOnScreen(False)

			#impostazione di velocità e posiz. muri in base allo score
			if score >= 2:
				speed = 12.5
			if score >= 4:
				speed = 15
			if score >= 6-1:
				position_of_wall_1 = [40, 100]
				body_of_wall_1 = []
				for x in range(0, 30):
					body_of_wall_1.append([(position_of_wall_1[0]+ (x*10)), 100])
					body_of_wall_1.append([(position_of_wall_1[0]+ (x*10)), 110])
			if score >= 8-1:
				position_of_wall_2 = [530,480]
				body_of_wall_2 = []
				for x in range(0, 30):
					body_of_wall_2.append([(position_of_wall_2[0]- (x*10)), 480])
					body_of_wall_2.append([(position_of_wall_2[0]- (x*10)), 490])
			if score >= 10-1:
				position_of_wall_3 = [100,530]
				body_of_wall_3 = []
				for x in range(0, 30):
					body_of_wall_3.append([100,(position_of_wall_3[1]- (x*10))])
					body_of_wall_3.append([110,(position_of_wall_3[1]- (x*10))])
			if score >= 12-1:
				position_of_wall_4 = [500, 330]  
				body_of_wall_4 = []
				for x in range(0, 30):
					body_of_wall_4.append([500, (position_of_wall_4[1]- (x*10))])
					body_of_wall_4.append([490, (position_of_wall_4[1]- (x*10))])
			if score >= 14-1:
				position_of_wall_5_1 = [230, 230]
				position_of_wall_5_2 = [330, 230]
				position_of_wall_5_3 = [150, 340]
				position_of_wall_5_4 = [240, 230]
				body_of_wall_5 = []
				for x in range(0, 10):
					body_of_wall_5.append([230, (position_of_wall_5_1[1]+ (x*10))])
					body_of_wall_5.append([240, (position_of_wall_5_1[1]+ (x*10))])
					body_of_wall_5.append([330, (position_of_wall_5_2[1]+ (x*10))])
					body_of_wall_5.append([340, (position_of_wall_5_2[1]+ (x*10))])
					body_of_wall_5.append([(position_of_wall_5_4[1]+ (x*10)), 240])
					body_of_wall_5.append([(position_of_wall_5_4[1]+ (x*10)), 230])
				for x in range(0, 12):
					body_of_wall_5.append([(position_of_wall_5_3[1]- (x*10)), 340])
					body_of_wall_5.append([(position_of_wall_5_3[1]- (x*10)), 350])
			
			#determina la vittoria
			if score == 16-1:
				bg = pygame.image.load('prato_bg.jpg')
				font = pygame.font.SysFont("Comfortaa", 150)
				surf_text = font.render("WIN", True, (0, 0, 0))
				screen.blit(surf_text, (200, 250))                            
				pygame.display.flip()
				done = False
				while not done:
					for ev in pygame.event.get():
							if ev.type == QUIT:
								done = True
					pygame.quit()
					sys.exit()


			#controllo posizionamento cibo
			x = 0
			if score >= 6-1:
				for x in range(0, len(body_of_wall_1)):
					if body_of_wall_1[x] == foodSpawner.spawnFood():
						foodSpawner.setFoodOnScreen(False)
						x = 0
					else:
						x += 1
			if score >= 8-1:
				for x in range(0, len(body_of_wall_2)):
					if body_of_wall_2[x] == foodSpawner.spawnFood():
						foodSpawner.setFoodOnScreen(False)
						x = 0
					else:
						x += 1
			if score >= 10-1:
				for x in range(0, len(body_of_wall_3)):
					if body_of_wall_3[x] == foodSpawner.spawnFood():
						foodSpawner.setFoodOnScreen(False)
						x = 0
					else:
						x += 1
			if score >= 12-1:
				for x in range(0, len(body_of_wall_4)):
					if body_of_wall_4[x] == foodSpawner.spawnFood():
						foodSpawner.setFoodOnScreen(False)
						x = 0
					else:
						x += 1
			if score >= 14-1:
				for x in range(0, len(body_of_wall_5)):
					if body_of_wall_5[x] == foodSpawner.spawnFood():
						foodSpawner.setFoodOnScreen(False)
						x = 0
					else:
						x += 1

			screen.blit(bg, [0, 0])


			#colorazione snake
			for pos in snake.getBody():
				pygame.draw.rect(screen, pygame.Color(225,218,228), pygame.Rect(pos[0], pos[1], 10, 10))

			#colorazione muri
			if score >= 6:
				for pos in body_of_wall_1:
					pygame.draw.rect(screen, pygame.Color(60,60,60), pygame.Rect(pos[0], pos[1], 10, 10))

			if score >= 8:
				for pos in body_of_wall_2:
					pygame.draw.rect(screen, pygame.Color(60,60,60), pygame.Rect(pos[0], pos[1], 10, 10))

			if score >= 10:
				for pos in body_of_wall_3:
					pygame.draw.rect(screen, pygame.Color(60, 60,60), pygame.Rect(pos[0], pos[1], 10, 10))

			if score >= 12:
				for pos in body_of_wall_4:
					pygame.draw.rect(screen, pygame.Color(60, 60,60), pygame.Rect(pos[0], pos[1], 10, 10))

			if score >= 14:
				for pos in body_of_wall_5:
					pygame.draw.rect(screen, pygame.Color(60, 60,60), pygame.Rect(pos[0], pos[1], 10, 10))

			#colorazione cibo
			pygame.draw.rect(screen, pygame.Color(231,0,0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

			#controllo scontro snake con muro
			a=0
			if score >= 6:
				for bodyPart in body_of_wall_1[1:]:
					for partOfBody in snake.body[:]:
						if partOfBody == bodyPart:
							a = 1
							break
			if score >= 8:
				for bodyPart in body_of_wall_2[1:]:
					for partOfBody in snake.body[:]:
						if partOfBody == bodyPart:
							a = 1
							break
			if score >= 10:
				for bodyPart in body_of_wall_3[1:]:
					for partOfBody in snake.body[:]:
						if partOfBody == bodyPart:
							a = 1
							break
			if score >= 12:
				for bodyPart in body_of_wall_4[1:]:
					for partOfBody in snake.body[:]:
						if partOfBody == bodyPart:
							a = 1
							break
			if score >= 14:
				for bodyPart in body_of_wall_5[1:]:
					for partOfBody in snake.body[:]:
						if partOfBody == bodyPart:
							a = 1
							break

			#perdita di vite legata a scontri
			if snake.checkCollision() == 1 or a == 1:
				life -= 1
				break

			#assegnazione partita persa
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


			#punteggio e vite
			#LIFE_SCORE = "LIFE: " + str(life) + "   SCORE: " + str(score)
			#bg = pygame.image.load('prato_bg.jpg')
			#font = pygame.font.SysFont("Comfortaa", 30)
			#surf_text = font.render(LIFE_SCORE, True, (255, 255, 255))
			#screen.blit(surf_text, (10, 10))                            
			#pygame.display.flip()
			#done = False
			#while True:
			#	for ev in pygame.event.get():
			#			if ev.type == QUIT:
			#				break
			#	break

			#spiegazione elementi presenti nel gioco
			#bg = pygame.image.load('prato_bg.jpg')
			#font = pygame.font.SysFont("Comfortaa", 20)
			#surf_text = font.render('SNAKE            FOOD            WALL', True, (255, 255, 255))
			#screen.blit(surf_text, (110, 555))                            
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