class Solution(object):
	def findFrequentTreeSum(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		d = dict()
		def dfs(root):
			if not root:
				return 0
			left = dfs(root.left)
			right = dfs(root.right)
			t = left+right+root.val
			if t not in d:
				d[t] = [1,t]
			else:
				d[t] = [d[t][0]+1,t]
			return t
		dfs(root)
		vals = d.values()
		vals.sort(key=lambda x:x[0],reverse=True)
		index = vals[0][0]
		res = []
		for i in vals:
			if index==i[0]:
				res.append(i[1])
			else:
				break
		return res