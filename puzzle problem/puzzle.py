import pygame
import time
from astar import Astar

def createBoard(n,a,display):

	f = pygame.font.Font(None,100)

	for i in range(n):
		for j in range(n):

			s = f.render(str(a[n*i+j]),True,(0,0,0),(255,255,255))

			r = s.get_rect()

			r.center = (j*pixels+pixels//2),(i*pixels+pixels//2)

			if a[n*i+j] > 0:

				pygame.draw.rect(display,(255,255,255),(j*pixels,i*pixels,pixels,pixels))
				display.blit(s,r)

			else:
				pygame.draw.rect(display,(0,200,200),(j*pixels,i*pixels,pixels,pixels))


			pygame.draw.rect(display,(0,0,0),(j*pixels,i*pixels,pixels,pixels),2)



	pygame.display.update()



def main():

	pygame.init()

	n = int(input("Enter grid size:"))

	res = (n*pixels,n*pixels)

	display = pygame.display.set_mode(res)

	s = ( (1,2,4,7,5,3,0,8,6),(2,0) )

	t = ( (1,2,3,4,5,6,7,8,0),(2,2) )


	algo = Astar(n,s,t)


	while True:


		if not algo.found:

			idx = algo.search()

			createBoard(n,idx[0],display)


			if idx == t:

				path = algo.createPath()

				time.sleep(3)

				for idx in path:

					createBoard(n,idx[0],display)
					
					time.sleep(2)



		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				exit()



pixels = 150
main()