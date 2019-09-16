class Solution(object):
	def isCompleteTree(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if(not root):
			return True
		res = []
		queue = []
		queue.append(root)
		res.append([root.val])
		while queue:
			size = len(queue)
			tmp = []
			for _ in xrange(size):
				node = queue.pop(0)
				if(node==None):
					queue.append(None)
					queue.append(None)
					tmp.append(None)
					tmp.append(None)
				else:
					if(node.left!=None):
						queue.append(node.left)
						tmp.append(node.left.val)
					else:
						queue.append(None)
						tmp.append(None)
					if(node.right!=None):
						queue.append(node.right)
						tmp.append(node.right.val)
					else:
						queue.append(None)
						tmp.append(None)
			# end for
			#check end,if queue->[None,None,None...] then break
			is_last_line = True #用于边界处理，如果tmp队列中全都是None，则说明处理完毕，退出循环
			for i in queue:
				if(i!=None):
					is_last_line = False
					break
			# has_none是false，说明不是最后一行
			if(not is_last_line):
				if(None in res[-1]):
					return False
			
			if(is_last_line):
				break
			res.append(tmp)
		# end while
		
		#print res
		arr = res[-1]
		size = len(arr)
		index = size-1
		while(index>=0):
			if(arr[index]==None):
				arr.pop()
			else:
				break
			index -= 1
		if(None in arr):
			return False
		return True