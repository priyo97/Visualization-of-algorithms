class BFS:

	def __init__(self,n,Sx,Sy,Tx,Ty):

		self.n = n
		self.Sx = Sx
		self.Sy = Sy
		self.Tx = Tx
		self.Ty = Ty

		self.visited = [[False for _ in range(n)] for _ in range(n)]
		self.prev = [[None for _ in range(n)] for _ in range(n)]
	
		self.q = [(Sx,Sy)]

		self.p = (-1,-1)

		self.visited[Sx][Sy] = True



	def search(self):

		t = self.q.pop(0)

		if t == (self.Tx,self.Ty):

			self.q = None

			return t, self.p



		N = self.neighbours(t,self.n)

		for (Nx,Ny) in N:

			if not self.visited[Nx][Ny]:

				self.q.append((Nx,Ny))
				self.visited[Nx][Ny] = True
				self.prev[Nx][Ny] = t

		
		temp = self.p
		
		self.p = t
	
		return t, temp


	def neighbours(self,t,r):

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

	def createPath(self):

		path = []

		while self.prev[self.Tx][self.Ty] != None:

			path.append(self.prev[self.Tx][self.Ty])
			self.Tx, self.Ty = self.prev[self.Tx][self.Ty]

		return path[::-1] 


