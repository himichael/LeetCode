class Solution(object):
	def rob(self, root):
		if not root:
			return 0
		d = dict()
		def dfs(root,status):
			if not root:
				return 0
			if (root,status) in d:
				return d[root,status]
			a,b,c = 0,0,0
			a = dfs(root.left,status) + dfs(root.right,status)
			if status:
				b = dfs(root.left,0) + dfs(root.right,0)
			else:
				c = dfs(root.left,1) + dfs(root.right,1) + root.val
			d[root,status] = max(a,b,c)
			return d[root,status]
		return dfs(root,0)
		
		
		
	# 树形DP
	def rob(self, root):
		if not root:
			return 0
		def dfs(root):
			if not root:
				return 0,0
			left_steal,left_no_steal = dfs(root.left)
			right_steal,right_no_steal = dfs(root.right)
			a = root.val + left_no_steal + right_no_steal
			b = left_steal + right_steal
			return max(a,b),b
		a,b = dfs(root)
		return max(a,b)