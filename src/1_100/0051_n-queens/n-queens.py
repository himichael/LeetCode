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