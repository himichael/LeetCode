class UnionFind(object):
	def __init__(self):
		n = 10000
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
		root_p = self.findRoot(p)
		root_q = self.findRoot(q)
		self.roots[root_q] = root_p
			
		
class Solution(object):
	def accountsMerge(self, accounts):
		"""
		:type accounts: List[List[str]]
		:rtype: List[List[str]]
		"""
		if not accounts:
			return []
		email_to_id = dict()
		email_to_name = dict()
		i = 0
		uf = UnionFind()
		for arr in accounts:
			name = arr[0]
			for email in arr[1:]:
				email_to_name[email] = name
				if email not in email_to_id:
					email_to_id[email] = i
					i += 1
				uf.union(email_to_id[arr[1]], email_to_id[email])
		ans = dict()
		for email in email_to_name:
			i = uf.findRoot( email_to_id[email] )
			ans.setdefault(i,[]).append(email)
			#arr.append(email)
		for component in ans.values():
			component.sort()
			n = email_to_name[component[0]]
			component.insert(0,n)
		return ans.values()