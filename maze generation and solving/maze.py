from utility import DFS,Grid,Astar
import pygame
import time

def main():

	n = int(input("Enter grid size:"))

	display = Grid(n,pixels)


	current = display.grid[0]

	algo = DFS(n,current,display.grid)

	running = True

	while running:

		if algo.stack:
			
			display.drawCanvas()

			display.drawCurrent(algo.current,(200,0,0))

			algo.search(display)

			# time.sleep(0.2)

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				running = False
				break



	Sx, Sy = [int(x) for x in input().split()]
	Tx, Ty = [int(x) for x in input().split()]



	algo = Astar(n,Sx,Sy,Tx,Ty,display.grid)
	
	while True:

		if not algo.found:

			t, prev = algo.search()

			draw(display.display,t[0],t[1])

			draw(display.display,prev[0],prev[1],color=False)

			pygame.display.update()

			time.sleep(.2)


			if t == (Tx,Ty):

				path = algo.createPath()

				drawCanvas(display.display,path,display.grid)
				continue	

		for event in pygame.event.get():

				if event.type == pygame.QUIT:
					exit()



# def draw(display,i,j,color=(200,0,0)):

# 	w = j * pixels
# 	h = i * pixels

# 	pygame.draw.rect(display,color,(w,h,pixels,pixels))



def draw(display,i,j,color=True):

	w = j * pixels
	h = i * pixels

	# print(display)

	if color:
		pygame.draw.rect(display,(200,0,0),(w,h,pixels,pixels))
	else:
		pygame.draw.rect(display,(255,255,255),(w,h,pixels,pixels))

	pygame.draw.rect(display,(0,0,0),(w,h,pixels,pixels),2)



def drawCanvas(display,path,grid):

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