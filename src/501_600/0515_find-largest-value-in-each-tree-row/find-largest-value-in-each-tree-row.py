class Solution(object):
	def largestValues(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		def dfs(root,index):
			if not root:
				return
			if len(res)<index:
				res.append([float("-inf")])
			#print "prepare -> "+str(root.val)+" index->"+str(index)
			if res[index-1][0]<root.val:
				res[index-1][0] = root.val
			dfs(root.left,index+1)
			dfs(root.right,index+1)
		dfs(root,1)
		return [res[i][0] for i in xrange(len(res))]