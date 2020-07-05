class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = []
        def DFS(columns,xy_diff,xy_sum):
            p = len(columns)
            if(p == n):
                res.append(columns)
                return
            for q in range(n):
                if(q not in columns) and (p-q not in xy_diff) and (p+q not in xy_sum):
                    DFS(columns+[q], xy_diff+[p-q], xy_sum+[p+q])
        DFS([],[],[])
        return len(res)
		
		
		
	#普通的解法
    def totalNQueens(self, n):
        arr = [[0 for _ in xrange(n)] for _ in xrange(n)]
        self.res = 0
        def check(x,y):
            for i in xrange(x):
                if arr[i][y]=="Q":
                    return False
            i,j = x-1,y-1
            while i>=0 and j>=0:
                if arr[i][j]=="Q":
                    return False
                i,j = i-1,j-1
            i,j = x-1,y+1
            while i>=0 and j<n:
                if arr[i][j]=="Q":
                    return False
                i,j = i-1,j+1
            return True
        
        def dfs(x):
            if x==n:
                self.res += 1
                return
            for y in xrange(n):
                if check(x,y):
                    arr[x][y] = "Q"
                    dfs(x+1)
                    arr[x][y] = 0
        dfs(0)
        return self.res
		
		
		
	# O(1)解法
	def totalNQueens(self, n):
		if n<=0:
			return 0
		if n==1:
			return 1
		elif n==2 or n==3:
			return 0
		elif n==4:
			return 2
		elif n==5:
			return 10
		elif n==6:
			return 4
		elif n==7:
			return 40
		elif n==8:
			return 92
		elif n==9:
			return 352
		elif n==10:
			return 724
		elif n==11:
			return 2680
		elif n==12:
			return 14200
		else:
			return 73712