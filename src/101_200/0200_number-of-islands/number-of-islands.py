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
                else:
                    continue
                    
        return self.count    