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