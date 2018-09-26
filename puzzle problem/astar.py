class Astar:

	def __init__(self,n,s,t):

		self.n = n
		self.s = s
		self.t = t
		self.distance = {s:0}
		self.visited = {}
		self.d = {1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),0:(2,2)}
		self.prev = {s:None}
		self.found = False

	
	def search(self):

		idx = self.min_distance()

		self.visited[idx] = True

		if idx == self.t:

			self.found = True

		else:

			N = self.neighbours(self.n,idx)

			for k in N:

				if not self.visited.get(k,False):

					if not self.distance.get(k,False):

						self.distance[k] = self.distance[idx] + 1
						self.prev[k] = idx

					else:

						if self.distance[idx] + 1 < self.distance[k]:

							self.distance[k] = self.distance[idx] + 1
							self.prev[k] = idx


		return idx


	def min_distance(self):


		max = 9999

		for i in self.distance:

			if not self.visited.get(i,False):

				sum = 0

				for j,k in enumerate(i[0]):

					r = j // self.n
					c = j % self.n

					sum += abs(r - self.d[k][0]) + abs(c - self.d[k][1])


				if self.distance[i] + sum < max:

					max = self.distance[i] + sum
					idx = i


		return idx


	def neighbours(self,n,idx):

		i,j = idx[1]

		q = []

		l = list(idx[0])

		if i-1 >= 0 :

			l[n*i+j], l[n*(i-1)+j] = l[n*(i-1)+j], l[n*i+j]

			q.append( (tuple(l),(i-1,j)) )

			l[n*i+j], l[n*(i-1)+j] = l[n*(i-1)+j], l[n*i+j]

		if i+1 < n :

			l[n*i+j], l[n*(i+1)+j] = l[n*(i+1)+j], l[n*i+j]

			q.append( (tuple(l),(i+1,j)) )

			l[n*i+j], l[n*(i+1)+j] = l[n*(i+1)+j], l[n*i+j]


		if j-1 >= 0 :

			l[n*i+(j-1)], l[n*i+j] = l[n*i+j], l[n*i+(j-1)]

			q.append( (tuple(l),(i,j-1)) )

			l[n*i+(j-1)], l[n*i+j] = l[n*i+j], l[n*i+(j-1)]

		if j+1 < n:

			l[n*i+(j+1)], l[n*i+j] = l[n*i+j], l[n*i+(j+1)]

			q.append( (tuple(l),(i,j+1)) )

			l[n*i+(j+1)], l[n*i+j] = l[n*i+j], l[n*i+(j+1)]
			



		return q


	def createPath(self):

		y = self.t
		path = [y]

		while self.prev[y] != None:

			path.append(self.prev[y])
			y = self.prev[y]

		return path[::-1]
