class Astar:

	def __init__(self,n,Sx,Sy,Tx,Ty):

		self.n = n
		self.Sx = Sx
		self.Sy = Sy
		self.Tx = Tx
		self.Ty = Ty

		self.visited = [[False for _ in range(n)] for _ in range(n)]
		self.distance = [[999 for _ in range(n)] for _ in range(n)]
		self.prev = [[None for _ in range(n)] for _ in range(n)]
	

		self.h = [[ ( (Tx - i)**2 + (Ty - j)**2 )**0.5 for j in range(n)] for i in range(n)]

		self.found = False

		self.p = (-1,-1)

		self.distance[Sx][Sy] = 0


	def search(self):

		t = self.min_distance()

		self.visited[t[0]][t[1]] = True

		if t == (self.Tx,self.Ty):

			self.found = True

			return t, self.p



		N = self.unvisited_neighbours(t,self.n)

		for (Nx,Ny) in N:

			if self.distance[t[0]][t[1]] + 1 < self.distance[Nx][Ny]:

				self.distance[Nx][Ny] = self.distance[t[0]][t[1]] + 1  
			
				self.prev[Nx][Ny] = t

		
		temp = self.p
		
		self.p = t
	
		return t, temp


	def unvisited_neighbours(self,t,r):

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
				if not self.visited[ x[i][0] ][ x[i][1] ]:
					n.append(x[i])

		return n

	

	def createPath(self):

		path = []

		while self.prev[self.Tx][self.Ty] != None:

			path.append(self.prev[self.Tx][self.Ty])
			self.Tx, self.Ty = self.prev[self.Tx][self.Ty]

		return path[::-1]

	

	def min_distance(self):

		m = 999

		for i in range(self.n):
			for j in range(self.n):

				if not self.visited[i][j]:

					if self.distance[i][j] + self.h[i][j] < m:

						m = self.distance[i][j] + self.h[i][j]
						idx = (i,j)

		return idx
