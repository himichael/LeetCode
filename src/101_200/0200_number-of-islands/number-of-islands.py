class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if( not grid or len(grid[0])==0 ):
            return 0
        n = len(grid)
        m = len(grid[0])
        self.count = 0
        def recursion(i,j):
            if( i<0 or i>=n or j<0 or j>=m ):
                return
            if( grid[i][j]=="0" ):
                return
            grid[i][j] = "0"
            recursion(i-1,j)
            recursion(i+1,j)
            recursion(i,j+1)
            recursion(i,j-1)
            
        for i in xrange(n):
            for j in xrange(m):
                if( grid[i][j]=="1" ):
                    recursion(i,j)
                    self.count += 1                    
        return self.count    
		

	# StefanPochmann 的一种极简写法
	# https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
    def numIslands(self, grid):
		def sink(i,j):
			if( 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]=='1' ):
				grid[i][j]='0'
				map( sink, (i-1,i+1,i,i), (j,j,j+1,j-1) )
				return 1
			return 0
		return sum( sink(i,j) for i in xrange(len(grid)) for j in xrange(len(grid[i])) )     
				
				
				
				