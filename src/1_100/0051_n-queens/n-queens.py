class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        def DFS(columns,xy_diff,xy_sum):
            p = len(columns)
            if(p == n):
                result.append(columns)
                return
            for q in range(n):
                if(q not in columns) and (p-q not in xy_diff) and (p+q not in xy_sum):
                    DFS(columns+[q], xy_diff+[p-q], xy_sum+[p+q])
        DFS([],[],[])
        print result
        return [ ["."*i + "Q" + "."*(n-i-1) for i in col] for col in result]
		
		
		
# 朴素的解法
class Solution(object):
    def solveNQueens(self, n):
        arr = [[0 for _ in xrange(n)] for _ in xrange(n)]
        res = []
        def check(x,y):
            for i in xrange(x):
                if arr[i][y]=='Q':
                    return False
            i = x-1
            j = y-1
            while i>=0 and j>=0:
                if arr[i][j]=='Q':
                    return False
                i -= 1
                j -= 1
            i = x-1
            j = y+1
            while i>=0 and j<=n-1:
                if arr[i][j]=='Q':
                    return False
                i -= 1
                j += 1
            return True
        
        def setup(x,y):
            arr[x][y] = 'Q'
            
        def recovery(x,y):
            arr[x][y] = 0
        
        def is_finish(x):
            if x==n-1:
                return True
            return False
        
        def save_res():
            ans = []
            for i in xrange(n):
                tmp = ""
                for j in xrange(n):
                    if arr[i][j]=='Q':
                        tmp += 'Q'
                    else:
                        tmp += '.'
                ans.append(tmp)
            return res.append(ans)
        
        def dfs(i):
            i += 1
            for j in xrange(n):
                if check(i,j):
                    setup(i,j)
                    if is_finish(i):
                        save_res()
                    else:
                        dfs(i)
                    recovery(i,j)
        dfs(-1)
        return res