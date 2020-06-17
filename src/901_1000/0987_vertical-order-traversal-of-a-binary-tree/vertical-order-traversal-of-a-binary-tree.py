class Solution(object):
	def verticalTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		d = collections.defaultdict(lambda: collections.defaultdict(list))
		def dfs(root,x,y):
			if not root:
				return
			d[x][y].append(root.val)
			dfs(root.left,x-1,y+1)
			dfs(root.right,x+1,y+1)
		dfs(root,0,0)
		res = []
		for x in sorted(d):
			report = []
			for y in sorted(d[x]):
				report.extend(sorted(v for v in d[x][y]))
			res.append(report)
		return res