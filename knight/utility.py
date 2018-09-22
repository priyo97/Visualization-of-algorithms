from dijkstra import Dijkstra
from astar import Astar
from bfs import BFS
import pygame
import time
import os


pixels = 50

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

def initiate(n):


	pygame.quit() # To destroy previously opened window
	pygame.init()

	os.environ['SDL_VIDEO_CENTERED'] = '1'
	
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

	return pos , gameDisplay


def placeEntity(entity,x,y,gameDisplay):
	
	gameDisplay.blit(entity,(x*pixels+5,y*pixels+5))


def loadEntity():

	knight = pygame.image.load("knight.png")

	yield 1,knight

	queen = pygame.image.load("queen.png")

	yield 2,queen


def markVisited(prevX,prevY,gameDisplay):

	pygame.draw.rect(gameDisplay,(200,0,0),(prevX*pixels+5,prevY*pixels+5,pixels-10,pixels-10))




def runDijkstra(n,pos,gameDisplay):

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



def runAstar(n,pos,gameDisplay):

	Sy, Sx = pos[1]
	Ty, Tx = pos[2]

	# Setting up images

	queen  = pygame.image.load("queen.png")

	knight = pygame.image.load("knight.png")
	
	
	
	# Initializing the board and the algo


	createChessboard(gameDisplay,n)
	
	placeEntity(queen,Ty,Tx,gameDisplay)	

	
	d = Astar(n,Sx,Sy,Tx,Ty)



	# game loop

	running = True

	while running:


		if not d.found:
			
			# returns current node and previous node

			t, prev = d.search()
		
			placeEntity(knight,t[1],t[0],gameDisplay)

			markVisited(prev[1],prev[0],gameDisplay)

			pygame.display.update()

			time.sleep(1)


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


def runBFS(n,pos,gameDisplay):

	Sy, Sx = pos[1]
	Ty, Tx = pos[2]


	# Setting up the screen and images

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


def runDFS(n,pos,gameDisplay):

	Sy, Sx = pos[1]
	Ty, Tx = pos[2]


	# Taking input from user

	visited = [[False for _ in range(n)] for _ in range(n)]

	p = (-1,-1)

	visited[Sx][Sy] = True


	# Setting up the screen and images

	queen  = pygame.image.load("queen.png")

	knight = pygame.image.load("knight.png")
	
	
	
	# Initializing the board and the algo


	createChessboard(gameDisplay,n)
	
	placeEntity(queen,Ty,Tx,gameDisplay)	



	# game loop

	running = True

	if dfs(n,visited,Sx,Sy,Tx,Ty,p,gameDisplay,knight):


		while running:

			for event in pygame.event.get():

					if event.type == pygame.QUIT:
						running = False
						break


	print("Target position ",(Tx,Ty)," reached: ",visited[Tx][Ty])

	pygame.quit()




def dfs(n,visited,Sx,Sy,Tx,Ty,prev,gameDisplay,knight):

	placeEntity(knight,Sy,Sx,gameDisplay)

	markVisited(prev[1],prev[0],gameDisplay)

	pygame.display.update()


	time.sleep(1)

	if (Sx,Sy) == (Tx,Ty):

			return True


	N = neighbours((Sx,Sy),n)


	for (Nx,Ny) in N:

		if not visited[Nx][Ny]:

			visited[Nx][Ny] = True

			if dfs(n,visited,Nx,Ny,Tx,Ty,(Sx,Sy),gameDisplay,knight):

				return True

			else:

				pygame.draw.rect(gameDisplay,(255,255,255),(Ny*pixels+5,Nx*pixels+5,pixels-10,pixels-10))

				placeEntity(knight,Sy,Sx,gameDisplay)

				pygame.display.update()

				time.sleep(1)



def neighbours(t,r):

		n = []
		x = [0]*8

		x[0] = t[0]+2, t[1]+1
		x[1] = t[0]+2, t[1]-1
		x[2] = t[0]-2, t[1]+1
		x[3] = t[0]-2, t[1]-1
		x[4] = t[0]+1, t[1]+2
		x[5] = t[0]+1, t[1]-2
		x[6] = t[0]-1, t[1]+2
		x[7] = t[0]-1, t[1]-2


		for i in range(8):
			if 0 <= x[i][0] < r and 0 <= x[i][1] < r:
				n.append(x[i])

		return n
