import pygame
import time
from astar import Astar

def drawBoard(n,a,display):

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
				pygame.draw.rect(display,(200,0,0),(j*pixels,i*pixels,pixels,pixels))


			pygame.draw.rect(display,(0,0,0),(j*pixels,i*pixels,pixels,pixels),2)



	pygame.display.update()



def createBoard(n,display):

	for i in range(n):
		for j in range(n):

			pygame.draw.rect(display,(255,255,255),(j*pixels,i*pixels,pixels,pixels))

			pygame.draw.rect(display,(0,0,0),(j*pixels,i*pixels,pixels,pixels),2)

	pygame.display.update()



def main():

	pygame.init()

	n = int(input("Enter grid size:"))

	res = (n*pixels,n*pixels)
	
	display = pygame.display.set_mode(res)

	createBoard(n,display)



	prev = (-1,-1)

	pos = set()

	counter = 1
	
	l = n*n

	a = [0]*l

	f = pygame.font.Font(None,100)


	running = True

	while running:

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				exit()

			elif event.type == pygame.MOUSEBUTTONUP:

				
				p = pygame.mouse.get_pos()

				x = p[0]//pixels
				y = p[1]//pixels

				s = f.render(str(counter),True,(0,0,0),(255,255,255))

				r = s.get_rect()

				r.center = (x*pixels+pixels//2),(y*pixels+pixels//2)

				display.blit(s,r)

				pygame.display.update()


				

				a[n*y+x] = counter

				pos.add((x,y))

				counter += 1


				if counter == l:
					running = False
					break


			elif event.type == pygame.MOUSEMOTION:

				p = pygame.mouse.get_pos()

				w = p[0]//pixels
				h = p[1]//pixels

				if (w,h) not in pos:
					
					if prev != (w,h):

						pygame.draw.rect(display,(200,0,0),(w*pixels,h*pixels,pixels,pixels))
						pygame.draw.rect(display,(0,0,0),(w*pixels,h*pixels,pixels,pixels),2)


						print("w h",(w,h),"prev",prev)

						if prev not in pos:

							pygame.draw.rect(display,(255,255,255),(prev[0]*pixels,prev[1]*pixels,pixels,pixels))
							pygame.draw.rect(display,(0,0,0),(w*pixels,h*pixels,pixels,pixels),2)

						pygame.display.update()

				else:

					if prev not in pos:

						pygame.draw.rect(display,(255,255,255),(prev[0]*pixels,prev[1]*pixels,pixels,pixels))
						pygame.draw.rect(display,(0,0,0),(w*pixels,h*pixels,pixels,pixels),2)

						pygame.display.update()

				prev = (w,h)




	return n, a, display



def run(n,a,display):


	# s = ( (1,2,4,7,5,3,0,8,6),(2,0) )

	# t = ( (1,2,3,4,5,6,7,8,0),(2,2) )

	for i in range(n*n):

		if a[i] == 0:

			idx = i




	s = ( tuple(a),(idx//n,idx % n) )


	a = []

	for i in range(1,n*n):

		a.append(i)

	a.append(0)

	t = ( tuple(a),(n-1,n-1) )




	algo = Astar(n,s,t)


	while True:


		if not algo.found:

			idx = algo.search()

			drawBoard(n,idx[0],display)


			if idx == t:

				path = algo.createPath()

				time.sleep(3)

				for idx in path:

					drawBoard(n,idx[0],display)
					
					time.sleep(2)



		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				exit()



pixels = 150
n, a, display = main()
run(n,a,display)
