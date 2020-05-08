class Solution(object):
	def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		if not matrix or not matrix[0]:
			return 0
		n = len(matrix)
		m = len(matrix[0])
		max_side = 0
		for i in xrange(n):
			for j in xrange(m):
				if matrix[i][j]=="1":
					max_side = max(max_side,1)
					current_max = min(n-i,m-j)
					for k in xrange(1,current_max):
						flag = True
						if matrix[i+k][j+k]=="0":
							break
						for v in xrange(k):
							if matrix[i+k][j+v]=="0" or matrix[i+v][j+k]=="0":
								flag = False
								break
						if flag:
							max_side = max(max_side,k+1)
						else:
							break
		return max_side**2
		
		
		
	# 动态规划
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in xrange(m)] for _ in xrange(n)]
        max_side = 0
        for i in xrange(n):
            dp[i][0] = 1 if matrix[i][0]=="1" else 0
            max_side = max(max_side,dp[i][0])
        for i in xrange(m):
            dp[0][i] = 1 if matrix[0][i]=="1" else 0
            max_side = max(max_side,dp[0][i])
        for i in xrange(1,n):
            for j in xrange(1,m):
                if matrix[i][j]=="1":
					dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
					max_side = max(max_side,dp[i][j])
        return max_side**2	
		
		
		