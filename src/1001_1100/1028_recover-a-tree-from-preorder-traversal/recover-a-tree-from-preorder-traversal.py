class Solution(object):
	def recoverFromPreorder(self, S):
		"""
		:type S: str
		:rtype: TreeNode
		"""	
		if not S:
			return None
		n = len(S)
		i = 0
		ans = []
		while i<n:
			level = 0
			while i<n and S[i]=="-":
				level += 1
				i += 1
			val = 0
			while i<n and S[i]>='0' and S[i]<='9':
				val = val*10 + ord(S[i])-48
				i += 1
			node = TreeNode(val)
			if level==len(ans):
				if ans:
					ans[-1].left = node
			else:
				while level!=len(ans):
					ans.pop()
				ans[-1].right = node
			ans.append(node)
		return ans[0]