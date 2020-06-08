class UnionFind(object):
	def __init__(self):
		self.roots = list(xrange(26))
	
	def find(self,i):
		root = i
		while root!=self.roots[root]:
			root = self.roots[root]
		while i!=self.roots[i]:
			tmp = self.roots[i]
			self.roots[i] = root
			i = tmp
		return root
	
	def union(self,p,q):
		root_p = self.find(p)
		root_q = self.find(q)
		self.roots[root_q] = root_p
		
		
class Solution(object):
	def equationsPossible(self, equations):
		if not equations:
			return True
		uf = UnionFind()
		for i in equations:
			if i[1]=="=":
				a = ord(i[0])-97
				b = ord(i[3])-97
				uf.union(a,b)
		for i in equations:
			if i[1]=="!":
				a = ord(i[0])-97
				b = ord(i[3])-97
				if uf.find(a)==uf.find(b):
					return False
		return True