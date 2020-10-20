class Graph:
	
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = [[None for i in range(vertices)] for i in range(vertices)]


	def addEdge(self, u, v, cost):
		if u < 0 or v < 0 or u >= self.vertices or v >= self.vertices:
			print("Vertex doesn't exist in the graph")
		else:
			self.graph[u][v] = cost
			self.graph[v][u] = cost


	def getClosest(self):
		m = float("inf")
		node = None
		for i in range(self.vertices):
			if self.dist[i] < m and self.mst[i] == False:
				m = self.dist[i]
				node = i
		return node, m


	def prim(self):
		self.mst = [False for i in range(self.vertices)]
		self.dist = [float("inf") for i in range(self.vertices)]
		self.parent = [i for i in range(self.vertices)]
		self.dist[0] = 0
		self.ans = []

		for i in range(self.vertices):
			node, cost = self.getClosest()
			self.ans.append([self.parent[node], node, self.graph[self.parent[node]][node]])
			self.mst[node] = True
			for neighbor in range(self.vertices):
				if (not self.mst[neighbor]) and (self.graph[node][neighbor]) and (self.dist[neighbor]>self.graph[node][neighbor]):
					self.dist[neighbor] = self.graph[node][neighbor]
					self.parent[neighbor] = node
		
		for row in self.ans:
			print(row)


if __name__ == "__main__":
	obj = Graph(9)	# Create a graph object with number of vertices
	# We can pass a graph or add individual edges
	obj.addEdge(0, 1, 4)	# Adding edge between 0 & 1 with weight 4
	obj.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
				[4, 0, 8, 0, 0, 0, 0, 11, 0],
				[0, 8, 0, 7, 0, 4, 0, 0, 2],
				[0, 0, 7, 0, 9, 14, 0, 0, 0],
				[0, 0, 0, 9, 0, 10, 0, 0, 0],
				[0, 0, 4, 14, 10, 0, 2, 0, 0],
				[0, 0, 0, 0, 0, 2, 0, 1, 6],
				[8, 11, 0, 0, 0, 0, 1, 0, 6],
				[0, 0, 2, 0, 0, 0, 6, 7, 0]]
	obj.prim()	# Calling the prim function to print the MST






