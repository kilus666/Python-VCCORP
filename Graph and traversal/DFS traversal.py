class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.discovery = 0
		self.finish = 0
		self.color = 'black'
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()
j=0
X=[]
time= 0
class Graph:
	vertices = {} 

	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False
			
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish))

		# Depth first traversal
	def _dfs(self, vertex):
		global time
		vertex.color = 'red'
		vertex.discovery = time
		time += 1
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs(self.vertices[v])
		vertex.color = 'blue'
		vertex.finish = time
		time += 1


	def dfs(self, vertex):
		global time
		time = 1
		self._dfs(vertex)
	
	
	# Breadth first traversal
	def bfs(self, vertex):
		global X
		global j
		if len(X)==0:
			vertex.color= 'red'
			vertex.discovery= j
			X.append(vertex)
			self.bfs(X[j])
		else:
			while j< len(X):
				for i in X[j].neighbors:
					if self.vertices[i].color== 'black':
						self.vertices[i].color= 'red'
						X.append(self.vertices[i])
						self.vertices[i].discovery= j+1
				j+=1


				
				

		


		
		
				
		
				
		
		



			
g = Graph()
# print(str(len(g.vertices)))
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])
	


g.dfs(a)
print(j)
g.print_graph()



