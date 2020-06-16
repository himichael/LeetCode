class Solution(object):
	def widthOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""		
		from collections import deque
		queue = deque()
		queue.append(root)
		max_len = float("-inf")
		while queue:
			while queue and queue[0]==None:
				queue.popleft()
			while queue and queue[-1]==None:
				queue.pop()
			size = len(queue)
			max_len = max(max_len,size)
			for _ in xrange(size):
				node = queue.popleft()
				if node:
					queue.append(node.left)
					queue.append(node.right)
				else:
					queue.append(None)
					queue.append(None)
		return max_len