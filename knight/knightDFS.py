import pygame
import time

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

	visited = [[False for _ in range(n)] for _ in range(n)]

	p = (-1,-1)

	visited[Sx][Sy] = True


	# Setting up the screen and images

	res = (n*pixels,n*pixels)

	gameDisplay = pygame.display.set_mode(res)

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

pixels = 50

main()
