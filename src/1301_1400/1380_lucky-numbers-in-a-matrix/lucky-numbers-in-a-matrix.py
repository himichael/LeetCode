class Solution(object):
    def luckyNumbers (self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        res = []
        for i in xrange(n):
            val = float("inf")
            index = -1
            for j in xrange(m):
                if val>matrix[i][j]:
                    val = matrix[i][j]
                    index = j
            is_max = True
            for j in xrange(n):
                if val<matrix[j][index]:
                    is_max = False
                    break               
            if is_max:
                res.append(val)
        return res