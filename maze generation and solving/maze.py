from utility import DFS,Grid,Astar
import pygame
import time
import os

position = (720,200)
os.environ['SDL_VIDEO_WINDOW_POS'] = str(position[0]) + "," + str(position[1])

def main():

	n = int(input("Enter grid size:"))

	display = Grid(n,pixels)


	current = display.grid[0]

	algo = DFS(n,current,display.grid)

	running = True

	
	red = (200,0,0)
	green = (0,200,0)

	while running:

		if algo.stack:
			
			display.drawCanvas()

			display.drawCurrent(algo.current,red)

			algo.search(display)

			# time.sleep(0.2)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				running = False
				break



	Sx, Sy = [int(x) for x in input("Enter source coords:").split()]
	Tx, Ty = [int(x) for x in input("Enter target coords:").split()]



	algo = Astar(n,Sx,Sy,Tx,Ty,display.grid)
	
	display.drawCanvas()

	while True:

		if not algo.found:

			t, prev = algo.search()

			display.drawCurrent(t,green)

			display.drawCurrent(prev,red)

			time.sleep(.2)


			if (t.i, t.j) == (Tx,Ty):

				path = algo.createPath()

				drawPath(display.display,path,display.grid)
				continue	

		for event in pygame.event.get():

				if event.type == pygame.QUIT:
					exit()




def drawPath(display,path,grid):

	display.fill((255,255,255))
		
	for c in grid:

		x = c.j 
		y = c.i

		if (y,x) in path:

			pygame.draw.rect(display,(150,0,0),(x*pixels+5,y*pixels+5,pixels-10,pixels-10))


		w = x * pixels
		h = y * pixels

		coord = ((w,h) , (w + pixels,h) , (w + pixels,h + pixels) , (w,h + pixels))
		

		for i in range(4):

			if c.sides[i]:

				pygame.draw.line( display, (0,0,0), coord[i], coord[ (i+1) % 4 ],4)

	

	pygame.display.update()





pixels = 50
main()
