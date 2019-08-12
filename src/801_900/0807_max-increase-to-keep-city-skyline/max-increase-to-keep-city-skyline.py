class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid_flip = []
        for i in range(len(grid)):
            tmp = []
            for j in range(len(grid[i])):
                tmp.append(grid[j][i])
            grid_flip.append(list(tmp))
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                y_max = max(grid_flip[j])
                x_max = max(grid[i])
                tmp = min(y_max,x_max)
                x = tmp - grid[i][j]
                #string = str(grid_flip[j]) +"=="+ str(grid[i]) + str(grid[i][j]) + "-->"+str(grid[i][j] in(y_max,x_max))
                #string += "  x="+str(x) + "tmp->"+str(tmp)+" y_max->"+str(y_max)+" x_max->"+str(x_max)
                #print string
                #if(x > 0):
                res += x
        return res