from utility import DFS,Grid
import pygame
import time

def main():


	n = int(input("Enter grid size:"))

	display = Grid(n,pixels)


	current = display.grid[0]

	algo = DFS(n,current,display.grid)


	while True:

		if algo.stack:
			
			display.drawCanvas()

			display.drawCurrent(algo.current)

			algo.search(display)

			time.sleep(0.2)

		

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				exit()





pixels = 50
main()