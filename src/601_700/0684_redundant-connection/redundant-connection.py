class UnionFind(object):
	def __init__(self,n):
		self.roots = [i for i in xrange(n+1)]
	
	def findRoot(self,i):
		root = i
		while root!=self.roots[root]:
			root = self.roots[root]
		while i!=self.roots[i]:
			tmp = self.roots[i]
			self.roots[i] = root
			i = tmp
		return root
	
	def isConnected(self,p,q):
		return self.findRoot(p)==self.findRoot(q)
		
	def union(self,p,q):
		qroot = self.findRoot(q)
		proot = self.findRoot(p)
		self.roots[proot] = qroot
		

class Solution(object):
	def findRedundantConnection(self, edges):
		"""
		:type edges: List[List[int]]
		:rtype: List[int]
		"""			
		if not edges:
			return []
		n = len(edges)
		uf = UnionFind(n)
		res = []
		uf.union(edges[0][0],edges[0][1])
		for i in xrange(1,n):
			if uf.isConnected(edges[i][0],edges[i][1]):
				res.append(edges[i][0])
				res.append(edges[i][1])
				break
			else:
				uf.union(edges[i][0],edges[i][1])
		return res