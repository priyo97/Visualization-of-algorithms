import pygame
import time
import os
from dijkstra import Dijkstra

os.environ['SDL_VIDEO_CENTERED'] = '1'

def createChessboard(gameDisplay,n):

	gameDisplay.fill((255,255,255))

	xdiff = pixels
	ydiff = pixels

	for h in range(n):
		for w in range(n):
			
			if (not h % 2 and not w % 2) or (h % 2 and w % 2):

					x = w * xdiff
					y = h * ydiff

					pygame.draw.rect(gameDisplay,(0,0,0),(x,y,xdiff,ydiff))


def loadEntity():

	knight = pygame.image.load("knight.png")

	yield 1,knight

	queen = pygame.image.load("queen.png")

	yield 2,queen



def placeEntity(entity,x,y,gameDisplay):
	
	gameDisplay.blit(entity,(x*pixels+5,y*pixels+5))



def main():

	pygame.init()

	# Taking input from user

	n = int(input("Enter grid size:"))


	
	# Setting up the screen

	res = (n*pixels,n*pixels)

	gameDisplay = pygame.display.set_mode(res)


	


	createChessboard(gameDisplay,n)

	pygame.display.update()

	prev = (-1,-1)

	pos = {}

	entity = loadEntity()

	running = True

	while running:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				exit()

			elif event.type == pygame.MOUSEBUTTONUP:

				p = pygame.mouse.get_pos()

				x = p[0]//50
				y = p[1]//50


				idx, e = next(entity)

				placeEntity(e,x,y,gameDisplay)

				pos[idx] = (x,y)

				pygame.display.update()

				if len(pos) == 2:

					running = False
					break



			elif event.type == pygame.MOUSEMOTION:

				p = pygame.mouse.get_pos()

				w = p[0]//50
				h = p[1]//50

				if (w,h) not in pos.values():
					
					if prev != (w,h):

						pygame.draw.rect(gameDisplay,(200,0,0),(w*50,h*50,50,50))

						print("w h",(w,h),"prev",prev)

						if prev not in pos.values():

							if (not prev[1] % 2 and not prev[0] % 2) or (prev[1] % 2 and prev[0] % 2):

								pygame.draw.rect(gameDisplay,(0,0,0),(prev[0]*50,prev[1]*50,50,50))
							
							else:
								pygame.draw.rect(gameDisplay,(255,255,255),(prev[0]*50,prev[1]*50,50,50))

						pygame.display.update()

				else:

					if prev not in pos.values():

						if (not prev[1] % 2 and not prev[0] % 2) or (prev[1] % 2 and prev[0] % 2):

							pygame.draw.rect(gameDisplay,(0,0,0),(prev[0]*50,prev[1]*50,50,50))
						
						else:
							pygame.draw.rect(gameDisplay,(255,255,255),(prev[0]*50,prev[1]*50,50,50))

						pygame.display.update()

				prev = (w,h)
	

	time.sleep(1)

	return n, pos , gameDisplay


def markVisited(prevX,prevY,gameDisplay):

	pygame.draw.rect(gameDisplay,(200,0,0),(prevX*pixels+5,prevY*pixels+5,pixels-10,pixels-10))



def rungame(n,pos,gameDisplay):

	pygame.init()

	Sy, Sx = pos[1]
	Ty, Tx = pos[2]

	# Setting up images

	queen  = pygame.image.load("queen.png")

	knight = pygame.image.load("knight.png")
	
	
	
	# Initializing the board and the algo


	createChessboard(gameDisplay,n)
	
	placeEntity(queen,Ty,Tx,gameDisplay)	

	d = Dijkstra(n,Sx,Sy,Tx,Ty)



	# game loop

	running = True

	while running:


		if not d.found:
			
			# returns current node and previous node

			t, prev = d.search()
		
			placeEntity(knight,t[1],t[0],gameDisplay)

			markVisited(prev[1],prev[0],gameDisplay)

			pygame.display.update()

			time.sleep(.2)


			if t == (Tx,Ty):

				createChessboard(gameDisplay,n)
				placeEntity(queen,Ty,Tx,gameDisplay)
				placeEntity(knight,Sy,Sx,gameDisplay)

				path = d.createPath()

				for i,j in path[1:]:

					markVisited(j,i,gameDisplay)

				pygame.display.update() 
		
				continue	

		for event in pygame.event.get():

				if event.type == pygame.QUIT:
					running = False
					break


	print("Target position ",(Tx,Ty)," reached: ",d.visited[Tx][Ty])

	pygame.quit()




pixels = 50

n, pos, gameDisplay = main()

rungame(n,pos,gameDisplay)
