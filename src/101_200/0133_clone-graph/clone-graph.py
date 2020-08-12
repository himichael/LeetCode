class Solution(object):
	def cloneGraph(self, node):
		"""
		:type node: Node
		:rtype: Node
		"""
		if not node:
			return None
		d = dict()
		def dfs(node):
			if not node:
				return
			if node in d:
				return d[node]
			d[node] = Node(node.val,[])
			for i in node.neighbors:
				d[node].neighbors.append( dfs(i) )
			return d[node]
		return dfs(node)