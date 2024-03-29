﻿# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
	mem = {0: [], 1: [TreeNode(0)]}
	def allPossibleFBT(self, n):
		"""
		:type n: int
		:rtype: List[TreeNode]
		"""
		if n not in Solution.mem:
			ans = []
			for x in range(n):
				y = n - 1 - x
				for left in self.allPossibleFBT(x):
					for right in self.allPossibleFBT(y):
						bns = TreeNode(0)
						bns.left = left
						bns.right = right
						ans.append(bns)
			Solution.mem[n] = ans
		return Solution.mem[n]
		
		