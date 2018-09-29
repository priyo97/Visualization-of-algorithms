import pygame
import random

pixels = 50


class Cell:

	def __init__(self,i,j):

		self.i = i
		self.j = j
		self.visited = False
		self.sides = [True,True,True,True]


class DFS:


	def __init__(self,n,current,grid):

		self.current = current
		self.current.visited = True
		self.n = n
		self.grid = grid
		self.stack = [current]

	def search(self,display):

		next = self.chooseNeighbour()

		if next:

			display.removeWalls(self.current,next)

			self.stack.append(self.current)

			self.current = next

			self.current.visited = True

		else:

			self.current = self.stack.pop()



	def chooseNeighbour(self):

		c = self.current

		i = c.i 
		j = c.j


		n = []

		# top
		if i - 1 >= 0 :

			idx = self.n*(i-1) + j

			if not self.grid[idx].visited:

				n.append(self.grid[idx])

		# right
		if j + 1 < self.n:


			idx = self.n*i + (j+1)

			if not self.grid[idx].visited:

				n.append(self.grid[idx])

		# bottom
		if i + 1 < self.n:

			idx = self.n*(i+1) + j

			if not self.grid[idx].visited:

				n.append(self.grid[idx])

		# left
		if j - 1 >= 0:

			idx = self.n*i + (j-1)

			if not self.grid[idx].visited:

				n.append(self.grid[idx])


		if len(n) > 0:
			m = random.randrange(len(n))
			return n[m]

		else:
			return None



class Grid:


	def __init__(self,n,pixels):

		pygame.init()

		self.n = n
		self.pixels = pixels
		self.res = (n*pixels,n*pixels)
		self.display = pygame.display.set_mode(self.res)

		self.grid = [ Cell(i,j) for i in range(n) for j in range(n) ]


	def drawCanvas(self):


		self.display.fill((255,255,255))
		
		for g in self.grid:

			self.showCell(g)

		
		pygame.display.update()


	def showCell(self,c):

		x = c.j 
		y = c.i


		w = x * self.pixels
		h = y * self.pixels

		coord = ((w,h) , (w + pixels,h) , (w + pixels,h + pixels) , (w,h + pixels))
		

		for i in range(4):

			if c.sides[i]:

				pygame.draw.line( self.display, (0,0,0), coord[i], coord[ (i+1) % 4 ] )



	def removeWalls(self,current,next):

		# print((current.i,current.j),(next.i,next.j))

		if next.i - current.i == 1:

			current.sides[2] = False
			next.sides[0] = False

		elif next.i - current.i == -1:

			current.sides[0] = False
			next.sides[2] = False


		elif next.j - current.j == 1:

			print("this one")

			current.sides[1] = False
			next.sides[3] = False

		elif next.j - current.j == -1:

			current.sides[3] = False
			next.sides[1] = False

	
	def drawCurrent(self,current):

		w = current.j * pixels
		h = current.i * pixels

		pygame.draw.rect(self.display,(200,0,0),(w,h,pixels,pixels))

		pygame.display.update()







