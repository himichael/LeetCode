class Graph(object):
	def __init__(self,vertexNum):
		self.__adjacencyTable = [[] for _ in xrange(vertexNum)]
	
	def addRelationOfVertices(self,src,dest):
		self.__adjacencyTable[src].append(dest)
	
	def vertexReference(self,i):
		return self.__adjacencyTable[i]
	
# BFS，Kahn算法	
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
		in_degree = [0 for _ in xrange(numCourses)]
		queue = []
		count = 0
		
		for arr in prerequisites:
			g.addRelationOfVertices(arr[1],arr[0])
		for i in xrange(numCourses):
			vertexes = g.vertexReference(i)
			for j in vertexes:
				in_degree[j] += 1
				
		for i in xrange(len(in_degree)):
			if in_degree[i]==0:
				queue.append(i)
				
		while queue:
			i = queue.pop(0)
			count += 1
			vertexes = g.vertexReference(i)
			for k in vertexes:
				in_degree[k] -= 1
				if in_degree[k]==0:
					queue.append(k)
		return count==numCourses
		
		
			
# DFS实现	
class Solution(object):
	def canFinish(self, numCourses, prerequisites):		
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: bool
		"""
		if numCourses<=0 or not prerequisites:
			return True
		inverseAdj = [[] for _ in xrange(numCourses)]
		for arr in prerequisites:
			inverseAdj[arr[0]].append(arr[1])
		visited = [0 for _ in xrange(numCourses)]
		for i in xrange(numCourses):
			if self.__checkLoop(i,inverseAdj,visited):
				return False
		return True
		
	# 0表示未访问，-1表示其他节点访问过了，1表示本节点正在访问	
	def __checkLoop(self,vertex,inverseAdj,visited):
		if visited[vertex]==-1:
			return False
		if visited[vertex]==1:
			return True
		visited[vertex] = 1	
		vertexes = inverseAdj[vertex]
		for i in vertexes:
			if self.__checkLoop(i,inverseAdj,visited):
				return True
		visited[vertex] = -1
		return False
		