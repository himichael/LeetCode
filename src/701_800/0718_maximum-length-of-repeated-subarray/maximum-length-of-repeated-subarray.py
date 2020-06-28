class Solution(object):
	def findLength(self, A, B):
		"""
		:type A: List[int]
		:type B: List[int]
		:rtype: int
		"""
		arr = [[-1]*len(B) for i in xrange(len(A))]
		res = 0
		for i in xrange(len(A)):
			for j in xrange(len(B)):
				if A[i]==B[j]:
					if i>0 and j>0:
						if arr[i-1][j-1]>0:
							arr[i][j] = arr[i-1][j-1]+1
						else:
							arr[i][j] = 1
						res = max(res,arr[i][j])
					else:
						arr[i][j] = 1
						res = max(res,arr[i][j])
		return res
		
		
		
	#精简的动态规划
	def findLength(self, A, B):
		dp = [[0 for _ in xrange(len(B)+1)] for _ in xrange(len(A)+1)]
		res = 0
		for i in xrange(1,len(A)+1):
			for j in xrange(1,len(B)+1):
				if A[i-1]==B[j-1]:
					dp[i][j] = dp[i-1][j-1]+1
				if dp[i][j]>res:
					res = dp[i][j]
		return res
		
		