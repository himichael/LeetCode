class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""
		if not board:
			return
		n = len(board)
		m = len(board[0])
		def dfs(i,j):
			if 0<=i<n and 0<=j<m and board[i][j]=="O":
				board[i][j] = "#"
				dfs(i,j+1)
				dfs(i,j-1)
				dfs(i+1,j)
				dfs(i-1,j)
		for i in xrange(n):
			dfs(i,0)
			dfs(i,m-1)
		for j in xrange(m):
			dfs(0,j)
			dfs(n-1,j)
		for i in xrange(n):
			for j in xrange(m):
				if board[i][j]=="O":
					board[i][j] = "X"
				if board[i][j]=="#":
					board[i][j] = "O"