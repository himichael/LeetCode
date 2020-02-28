class Graph(object):
	def __init__(self,v):
		self.vertex = v
		self.adj = [[] for _ in xrange(self.vertex)]
	def add_edge(self,s,t):
		self.adj[s].append(t)
	def get_vertex_edge(self,v):
		return self.adj[v]
	
class Solution(object):
	def canFinish(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		if numCourses<=0 or not prerequisites:
			return True
		g = Graph(numCourses)
		for arr in prerequisites:
			g.add_edge(arr[0],arr[1])
		
		in_degree = [0 for _ in xrange(numCourses)]
		for i in xrange(len(in_degree)):
			vertexs = g.get_vertex_edge(i)
			for j in vertexs:
				in_degree[j] += 1
		queue = []
		for i in xrange(len(in_degree)):
			if in_degree[i]==0:
				queue.append(i)
		while queue:
			i = queue.pop(0)
			numCourses -= 1
			vertexs = g.get_vertex_edge(i)
			for j in vertexs:
				in_degree[j] -= 1
				if in_degree[j]==0:
					queue.append(j)
		return numCourses==0