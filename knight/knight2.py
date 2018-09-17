import pygame
import time

def createChessboard(gameDisplay,n):

	gameDisplay.fill((255,255,255))

	xdiff = 50
	ydiff = 50

	for h in range(n):
		for w in range(n):
			if not h % 2:
				if not w % 2: 

					x = w*xdiff
					y = h*ydiff

					pygame.draw.rect(gameDisplay,(0,0,0),(x,y,xdiff,ydiff))

			else:
				if w % 2: 

					x = w*xdiff
					y = h*ydiff

					pygame.draw.rect(gameDisplay,(0,0,0),(x,y,xdiff,ydiff))



def initializeQueen(x,y,gameDisplay):

	queen  = pygame.image.load("queen.png")
	
	gameDisplay.blit(queen,(x*50+5,y*50+5))



def main():

	pygame.init()

	n = int(input("Enter grid size:"))

	Sx, Sy = [int(x) for x in input("Enter knight coords:").split()]
	Tx, Ty = [int(x) for x in input("Enter queen coords:").split()]


	visited = [[False for _ in range(n)] for _ in range(n)]

	q = (Sx,Sy)

	visited[Sx][Sy] = True

	



	res = (400,400)

	gameDisplay = pygame.display.set_mode(res)


	createChessboard(gameDisplay,n)

	initializeQueen(Ty,Tx,gameDisplay)

	
	knight = pygame.image.load("knight.png")
	

	running = True

	flag = 0

	while running:


		if q:

			t = q

			gameDisplay.blit(knight,(t[1]*50+5,t[0]*50+5))

			if flag:

				pygame.draw.rect(gameDisplay,(200,0,0),(prevX*50+5,prevY*50+5,50-10,50-10))

			
			prevX,prevY = t[1],t[0]

			flag = 1

			pygame.display.update()

			time.sleep(1)


			if t == (Tx,Ty):

				q = None
				continue


			q = neighbours(t,n,visited)

			if q == None:
				continue

			visited[ q[0] ][ q[1] ] = True


		for event in pygame.event.get():

			if event.type == pygame.QUIT:
					
				running = False
				break



	print("Target position ",(Tx,Ty)," reached: ",visited[Tx][Ty])

	pygame.quit()
	


def neighbours(t,r,visited):

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

			if not visited[ x[i][0] ][ x[i][1] ]:
				
				return x[i]




main()
