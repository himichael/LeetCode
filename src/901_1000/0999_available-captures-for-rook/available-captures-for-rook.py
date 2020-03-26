class Solution(object):
	def numRookCaptures(self, board):
		"""
		:type board: List[List[str]]
		:rtype: int
		"""	
		if not board:
			return 0
		N = 8
		r = -1
		c = -1
		dx = [0,1,0,-1]
		dy = [1,0,-1,0]
		res = 0
		for i in xrange(N):
			for j in xrange(N):
				if board[i][j]=="R":
					r = i
					c = j
					break
		for k in xrange(4):
			for step in xrange(N):
				x = r + step*dx[k]
				y = c + step*dy[k]
				if 0>x or x>=N or 0>y or y>=N or board[x][y]=="B":
					break
				if board[x][y]=="p":
					res += 1
					break
		return res