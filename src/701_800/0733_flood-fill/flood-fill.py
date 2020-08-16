class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if not image:
            return image
        n = len(image)
        m = len(image[0])
        val = image[sr][sc]
        def dfs(i,j):
            if 0<=i<n and 0<=j<m and image[i][j]==val:
                image[i][j] = newColor
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i-1,j)
        if newColor!=val:
            dfs(sr,sc)
        return image