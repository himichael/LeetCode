class Solution(object):
	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""		
		if not board:
			return
		board_bak = copy.deepcopy(board)						
		N = len(board)
		M = len(board[0])
		for i in xrange(N):
			for j in xrange(M):
				ans = self.liveOrDead(board,i,j)
				if ans==1:
					board_bak[i][j] = 1
				elif ans==2:
					board_bak[i][j] = 0
				else:
					pass
		for i in xrange(N):
			for j in xrange(M):
				board[i][j] = board_bak[i][j]
		
		
	def liveOrDead(self,arr,i,j):
		direction = [(-1,-1),(-1,1),(1,-1),(1,1),(0,1),(1,0),(-1,0),(0,-1)]
		N,M = len(arr),len(arr[0])
		live_count = 0
		for k in direction:
			x = i + k[0]
			y = j + k[1]
			if 0<=x<N and 0<=y<M and arr[x][y]==1:
				live_count += 1
		if live_count<2 or live_count>3:
			return 2
		elif arr[i][j]==1 or (arr[i][j]==0 and live_count==3):
			return 1
		else:
			return 0
			
			
			
			
	# 另一种实现
	def gameOfLife(self, board):
		if not board:
			return 
		direct = [(1,1),(1,-1),(-1,1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]
		N = len(board)
		M = len(board[0])
		for i in xrange(N):
			for j in xrange(M):
				live_count = 0
				for k in direct:
					x = i + k[0]
					y = j + k[1]
					if 0<=x<N and 0<=y<M:
						live_count += board[x][y] & 1
				if board[i][j] and 2<=live_count<=3:
					board[i][j] = 3
				if not board[i][j] and live_count==3:
					board[i][j] = 2
		for i in xrange(N):
			for j in xrange(M):
				board[i][j] >>= 1
				