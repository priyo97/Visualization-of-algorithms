import pygame
import time

def createChessboard(gameDisplay):

	gameDisplay.fill((255,255,255))

	xdiff = 50
	ydiff = 50

	for h in range(8):
		for w in range(8):
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

	visited = [[False for _ in range(n)] for _ in range(n)]

	Sx, Sy = [int(x) for x in input().split()]
	Tx, Ty = [int(x) for x in input().split()]

	q = [(Sx,Sy)]

	visited[Sx][Sy] = True

	

	res = (400,400)

	gameDisplay = pygame.display.set_mode(res)


	createChessboard(gameDisplay)

	initializeQueen(Ty,Tx,gameDisplay)

	knight = pygame.image.load("knight.png")
	
	flag = 0

	running = True

	while running:

		for event in pygame.event.get():

				if event.type == pygame.QUIT:
					running = False
					break

		while q:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					running = False
					break

			t = q.pop(0)

			gameDisplay.blit(knight,(t[1]*50+5,t[0]*50+5))

			if flag:

				pygame.draw.rect(gameDisplay,(200,0,0),(prevX*50+5,prevY*50+5,50-10,50-10))
				print(prevX,prevY)


			prevX,prevY = t[1],t[0]

			flag = 1

			pygame.display.update()

			time.sleep(1)


			if t == (Tx,Ty):

				q = []
				break


			N = neighbours(t,n)

			for (Nx,Ny) in N:

				if not visited[Nx][Ny]:

					q.append((Nx,Ny))
					visited[Nx][Ny] = True

		# print("Target position ",(Tx,Ty)," reached: ",visited[Tx][Ty])




	pygame.quit()

	

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


main()