class NumMatrix(object):

    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        self.dp = [[0] * (n + 1) for _ in range(m + 1)]
        d = self.dp
        for i in range(m):
            for j in range(n):
                d[i + 1][j + 1] = d[i + 1][j] + d[i][j + 1] - d[i][j] + matrix[i][j]
 

    def sumRegion(self, row1, col1, row2, col2):
        d = self.dp
        return d[row2 + 1][col2 + 1] - d[row1][col2 + 1] - d[row2 + 1][col1] + d[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)