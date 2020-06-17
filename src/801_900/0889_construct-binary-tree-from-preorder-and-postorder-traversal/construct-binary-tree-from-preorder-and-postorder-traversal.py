class Solution(object):
	def constructFromPrePost(self, pre, post):
		"""
		:type pre: List[int]
		:type post: List[int]
		:rtype: TreeNode
		"""	
		def dfs(pre,post):
			if not pre:
				return None
			if len(pre)==1:
				return TreeNode(pre[0])
			root = TreeNode(pre[0])
			left_count = post.index(pre[1])+1
			root.left = dfs(pre[1:left_count+1],post[:left_count])
			root.right = dfs(pre[left_count+1:],post[left_count:-1])
			return root
		return dfs(pre,post)