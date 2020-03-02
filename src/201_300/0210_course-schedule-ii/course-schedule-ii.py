class Solution(object):
	# BFS，Kahn算法
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		if numCourses<=0:
			return []
		if len(prerequisites)==0:
			return [i for i in xrange(numCourses)]
		adj = [[] for _ in xrange(numCourses)]
		in_degree = [0 for _ in xrange(numCourses)]
		queue = []
		res = []
		count = 0
		for second,first in prerequisites:
			adj[first].append(second)
			in_degree[second] += 1
		for i in xrange(len(in_degree)):
			if in_degree[i]==0:
				queue.append(i)
		while queue:
			i = queue.pop(0)
			res.append(i)
			count += 1
			for j in adj[i]:
				in_degree[j] -= 1
				if in_degree[j]==0:
					queue.append(j)
		return res if count==numCourses else []
		
		
	# DFS 实现
	def findOrder(self, numCourses, prerequisites):
		"""
		:type numCourses: int
		:type prerequisites: List[List[int]]
		:rtype: List[int]
		"""
		if numCourses<=0:
			return []
		if not prerequisites:
			return [i for i in xrange(numCourses)]
		inverse_adj = [[] for _ in xrange(numCourses)]
		visited = [0 for _ in xrange(numCourses)]
		for second,first in prerequisites:
			inverse_adj[second].append(first)
		res = []
		def dfs(i):
			if visited[i]==-1:
				return False
			if visited[i]==1:
				return True
			visited[i] = 1
			for j in inverse_adj[i]:
				if dfs(j):
					return True
			visited[i] = -1
			res.append(i)
		for i in xrange(len(inverse_adj)):
			if dfs(i):
				return []
		return res