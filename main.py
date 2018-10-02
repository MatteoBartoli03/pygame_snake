import pygame, sys, random, time
from class_snake import Snake
from pygame.locals import *
from time import gmtime, strftime

#variabili di base (num = lunghezza del serpente)
life = 5
speed = 10
score = 0
num = 0

#inizializzazione di pygame
pygame.init()

#impostazione finestra
screen = pygame.display.set_mode((580, 580))
bg = pygame.image.load('prato_bg.jpg')
ICON = pygame.image.load('ICON.png')	
pygame.display.set_icon(ICON)
pygame.display.set_caption("Snake game by Francesco & Matteo")
fps = pygame.time.Clock()

#definiamo la funzione GAME OVER
def gameOver():
	pygame.quit()
	sys.exit()

while True:
	from class_food import foodSpawner

	#assegnamento variabili importate da class_food e class_snake
	if score > 10:
		num = 10
	else:
		num = score

	snake = Snake(num)
	foodSpawner = foodSpawner()

	while True:
		#assegnazione partita persa
		if life == 0:
			bg = pygame.image.load('prato_bg.jpg')
			font = pygame.font.SysFont("Comfortaa", 100)
			surf_text = font.render("GAME OVER", True, (255,255, 255))
			screen.blit(surf_text, (60, 250))                            
			pygame.display.flip()
			pygame.time.delay(1000)
			gameOver()

		#assegnazione partita vinta
		if score == 30:
			pygame.time.delay(250)
			bg = pygame.image.load('prato_bg.jpg')
			font = pygame.font.SysFont("Comfortaa", 90)
			surf_text = font.render("YOU'VE WIN", True, (255,255, 255))
			screen.blit(surf_text, (100, 230))
			pygame.display.flip()
			pygame.time.delay(1000)
			gameOver()
			
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
		if score >= 5:
			speed = 12.5
		if score >= 10:
			speed = 15
		if score >= 14:
			position_of_wall_1 = [40, 100]
			body_of_wall_1 = []
			for x in range(0, 30):
				body_of_wall_1.append([(position_of_wall_1[0]+ (x*10)), 100])
				body_of_wall_1.append([(position_of_wall_1[0]+ (x*10)), 110])
		if score >= 17:
			position_of_wall_2 = [530,480]
			body_of_wall_2 = []
			for x in range(0, 30):
				body_of_wall_2.append([(position_of_wall_2[0]- (x*10)), 480])
				body_of_wall_2.append([(position_of_wall_2[0]- (x*10)), 490])
		if score >= 20:
			position_of_wall_3 = [100,530]
			body_of_wall_3 = []
			for x in range(0, 30):
				body_of_wall_3.append([100,(position_of_wall_3[1]- (x*10))])
				body_of_wall_3.append([110,(position_of_wall_3[1]- (x*10))])
		if score >= 23:
			position_of_wall_4 = [500, 330]  
			body_of_wall_4 = []
			for x in range(0, 30):
				body_of_wall_4.append([500, (position_of_wall_4[1]- (x*10))])
				body_of_wall_4.append([490, (position_of_wall_4[1]- (x*10))])
		if score >= 26:
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
		
		#controllo posizionamento cibo (su un muro)
		x = 0
		if score >= 14:
			for x in range(0, len(body_of_wall_1)):
				if body_of_wall_1[x] == foodSpawner.spawnFood():
					foodSpawner.setFoodOnScreen(False)
					x = 0
				else:
					x += 1
		if score >= 17:
			for x in range(0, len(body_of_wall_2)):
				if body_of_wall_2[x] == foodSpawner.spawnFood():
					foodSpawner.setFoodOnScreen(False)
					x = 0
				else:
					x += 1
		if score >= 20:
			for x in range(0, len(body_of_wall_3)):
				if body_of_wall_3[x] == foodSpawner.spawnFood():
					foodSpawner.setFoodOnScreen(False)
					x = 0
				else:
					x += 1
		if score >= 23:
			for x in range(0, len(body_of_wall_4)):
				if body_of_wall_4[x] == foodSpawner.spawnFood():
					foodSpawner.setFoodOnScreen(False)
					x = 0
				else:
					x += 1
		if score >= 26:
			for x in range(0, len(body_of_wall_5)):
				if body_of_wall_5[x] == foodSpawner.spawnFood():
					foodSpawner.setFoodOnScreen(False)
					x = 0
				else:
					x += 1

		screen.blit(bg, [0, 0])


		#colorazione snake
		for pos in snake.getBody():
			pygame.draw.rect(screen, pygame.Color(255,255,255), pygame.Rect(pos[0], pos[1], 10, 10))

		#colorazione muri
		if score >= 14:
			for pos in body_of_wall_1:
				pygame.draw.rect(screen, pygame.Color(60,60,60), pygame.Rect(pos[0], pos[1], 10, 10))

		if score >= 17:
			for pos in body_of_wall_2:
				pygame.draw.rect(screen, pygame.Color(60,60,60), pygame.Rect(pos[0], pos[1], 10, 10))

		if score >= 20:
			for pos in body_of_wall_3:
				pygame.draw.rect(screen, pygame.Color(60, 60,60), pygame.Rect(pos[0], pos[1], 10, 10))

		if score >= 23:
			for pos in body_of_wall_4:
				pygame.draw.rect(screen, pygame.Color(60, 60,60), pygame.Rect(pos[0], pos[1], 10, 10))

		if score >= 26:
			for pos in body_of_wall_5:
				pygame.draw.rect(screen, pygame.Color(60, 60,60), pygame.Rect(pos[0], pos[1], 10, 10))

		#colorazione cibo
		pygame.draw.rect(screen, pygame.Color(231,0,0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))

		#controllo scontro snake con muro
		a=0
		if score >= 14:
			for bodyPart in body_of_wall_1[1:]:
				if snake.getPos() == bodyPart:
					a = 1
					break
		if score >= 17:
			for bodyPart in body_of_wall_2[1:]:
				if snake.getPos() == bodyPart:
					a = 1
					break
		if score >= 20:
			for bodyPart in body_of_wall_3[1:]:
				if snake.getPos() == bodyPart:
					a = 1
					break
		if score >= 23:
			for bodyPart in body_of_wall_4[1:]:
				if snake.getPos() == bodyPart:
					a = 1
					break
		if score >= 26:
			for bodyPart in body_of_wall_5[1:]:
				if snake.getPos() == bodyPart:
					a = 1
					break

		#perdita di vite legata a scontri
		if snake.checkCollision() == 1 or a == 1:
			life -= 1
			break

		#punteggio e vite
		LIFE_SCORE = "LIFE: " + life * '♥' + "   SCORE: " + str(score)
		font = pygame.font.SysFont("Comfortaa", 30)
		surf_text = font.render(LIFE_SCORE, True, (255, 0, 0))
		screen.blit(surf_text, (10, 10))                            
		pygame.display.flip()
		fps.tick(speed)


	#comparsa scritte punteggio
	if snake.checkCollision() == 1 or a == 1:
		if life != 0:
			bg = pygame.image.load('prato_bg.jpg')
			font = pygame.font.SysFont("Comfortaa", 100)
			surf_text = font.render('LIFE :  '+ str(life), True, (255,255, 255))
			screen.blit(surf_text, (150, 230))                            
			pygame.display.flip()
			pygame.time.delay(250)
			done = False
			