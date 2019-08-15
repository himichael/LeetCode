"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		if(root == None):
			return root
		queue = []
		queue.append(root)
		
		while(queue):
			tmp = queue[0]
			for i in range(1,len(queue)):
				tmp.next = queue[i]
				tmp = queue[i]
			size = len(queue)
			for i in range(size):
				tmp = queue.pop(0)
				if(tmp.left != None):
					queue.append(tmp.left)
				if(tmp.right != None):
					queue.append(tmp.right)
		return root	