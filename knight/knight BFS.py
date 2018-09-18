import pygame
import time
from bfs import BFS

def createChessboard(gameDisplay,n):

	gameDisplay.fill((255,255,255))

	xdiff = pixels
	ydiff = pixels

	for h in range(n):
		for w in range(n):
			if (not h % 2 and not w % 2) or (h % 2 and w % 2):

					x = w*xdiff
					y = h*ydiff

					pygame.draw.rect(gameDisplay,(0,0,0),(x,y,xdiff,ydiff))


def placeEntity(entity,x,y,gameDisplay):
	
	gameDisplay.blit(entity,(x*pixels+5,y*pixels+5))



def markVisited(prevX,prevY,gameDisplay):

	pygame.draw.rect(gameDisplay,(200,0,0),(prevX*pixels+5,prevY*pixels+5,pixels-10,pixels-10))



def main():

	pygame.init()


	# Taking input from user

	n = int(input("Enter grid size:"))

	Sx, Sy = [int(x) for x in input("Enter knight coords:").split()]
	Tx, Ty = [int(x) for x in input("Enter queen coords:").split()]

	

	# Setting up the screen and images

	res = (n*pixels,n*pixels)

	gameDisplay = pygame.display.set_mode(res)

	queen  = pygame.image.load("queen.png")

	knight = pygame.image.load("knight.png")
	
	
	
	# Initializing the board and the algo


	createChessboard(gameDisplay,n)
	
	placeEntity(queen,Ty,Tx,gameDisplay)	

	b = BFS(n,Sx,Sy,Tx,Ty)



	# game loop

	running = True

	while running:


		if b.q:
			
			# returns current node and previous node

			t, prev = b.search()
		
			placeEntity(knight,t[1],t[0],gameDisplay)

			markVisited(prev[1],prev[0],gameDisplay)

			pygame.display.update()

			time.sleep(1)


			if t == (Tx,Ty):

				createChessboard(gameDisplay,n)
				placeEntity(queen,Ty,Tx,gameDisplay)
				placeEntity(knight,Sy,Sx,gameDisplay)

				path = b.createPath()

				for i,j in path[1:]:

					markVisited(j,i,gameDisplay)

				pygame.display.update() 
		
				continue

			if b.q == []:

				
				createChessboard(gameDisplay,n)
				
				cross = pygame.image.load("cross.jpg")

				placeEntity(cross,Ty,Tx,gameDisplay)
				placeEntity(knight,Sy,Sx,gameDisplay)

				pygame.display.update()
				

		for event in pygame.event.get():

				if event.type == pygame.QUIT:
					running = False
					break


	print("Target position ",(Tx,Ty)," reached: ",b.visited[Tx][Ty])

	pygame.quit()


pixels = 50

main()
