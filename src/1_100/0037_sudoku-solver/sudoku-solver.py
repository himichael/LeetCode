class Solution(object):
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: None Do not return anything, modify board in-place instead.
		"""
		N = 9
		horizontal  = [set() for _ in xrange(N)]
		vertical  = [set() for _ in xrange(N)]
		area = [[set() for _ in xrange(N//3)] for _ in xrange(N//3)]
		self.is_finish = False
		for i in xrange(N):
			for j in xrange(N):
				v = board[i][j]
				if v==".":
					continue
				horizontal[i].add(v)
				vertical[j].add(v)
				area[i//3][j//3].add(v)
		
		def setup(x,y,i):
			horizontal[x].add(i)
			vertical[y].add(i)
			area[x//3][y//3].add(i)
			board[x][y] = i
		
		def recovery(x,y,i):
			area[x//3][y//3].discard(i)
			vertical[y].discard(i)
			horizontal[x].discard(i)
			board[x][y] = "."
			
		def can_place(x,y,i):
			a = i not in horizontal[x]
			b = i not in vertical[y]
			c = i not in area[x//3][y//3]
			return a and b and c
			
		def go_next(x,y):
			if x==N-1 and y==N-1:
				self.is_finish = True
			else:
				x = (x+1)%N
				y = y+1 if x==0 else y
				backtrack(x,y)
		
		def backtrack(x,y):
			if board[x][y]!=".":
				go_next(x,y)
			else:
				for i in xrange(1,10):
					index = str(i)
					if can_place(x,y,index):
						setup(x,y,index)
						go_next(x,y)
						if not self.is_finish:
							recovery(x,y,index)
		backtrack(0,0)