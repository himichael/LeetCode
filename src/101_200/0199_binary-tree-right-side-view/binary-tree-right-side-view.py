# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if(root==None):
			return []
		res = []
		queue = []
		queue.append(root)
		while(queue):
			res.append(queue[-1].val)
			size = len(queue)
			for i in range(size):
				tmp = queue.pop(0)
				if(tmp.left != None):
					queue.append(tmp.left)
				if(tmp.right != None):
					queue.append(tmp.right)
		return res
		
		
	# 另一种解法 BFS方式，遍历节点后将用dict记录最后一个节点和深度
	def rightSideView(self, root):
		if not root:
			return []
		max_depth = -1
		queue = [(root,0)]
		right_view_map = dict()
		while queue:
			node,depth = queue.pop(0)
			max_depth = max(max_depth,depth)
			if node:
				right_view_map[depth] = node.val
				queue.append((node.left,depth+1))
				queue.append((node.right,depth+1))
		ans = []
		for v in right_view_map.values():
			ans.append(v)
		return ans
		
		
		
	# 跟解法二类似，只是改成stack了
	def rightSideView(self, root):		
		if not root:
			return []
		stack = [(root,0)]
		max_depth = -1
		right_view_map = dict()
		while stack:
			node,depth = stack.pop()
			if node:
				max_depth = max(max_depth,depth)
				if depth not in right_view_map:
					right_view_map[depth] = node.val
				stack.append((node.left,depth+1))
				stack.append((node.right,depth+1))
		return [right_view_map[depth] for depth in xrange(max_depth+1)]


		
	# 另一种DFS 实现，很巧妙
	def rightSideView(self, root):		
		ans = []
		def dfs(root,depth):
			if not root:
				return
			if depth==len(ans):
				ans.append(root.val)
			dfs(root.right,depth+1)
			dfs(root.left, depth+1)
		dfs(root,0)
		return ans		
		
		