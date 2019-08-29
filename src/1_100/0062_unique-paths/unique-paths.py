class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if(m==0 or n==0):
            return 0
        if(m==1 or n==1):
            return 1
        arr = [ [0 for _ in xrange(m)] for _ in xrange(n) ]
        i,j = 0,0
        while i<m:
            arr[0][i] = 1
            i +=1
        while j<n:
            arr[j][0] = 1
            j += 1
        
        i,j = 0,0
        while i<n-1:
            j = 0
            while j<m-1:
                arr[i+1][j+1] = arr[i+1][j] + arr[i][j+1]
                j += 1
            i += 1
        #for a in arr:
        #    print a
        return arr[n-1][m-1]