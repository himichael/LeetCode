class Solution(object):
    def cherryPickup(self, grid):
        cache = {}
        n = len(grid)
        def dfs(r1, c1, r2, c2):
            if (r1,c1,r2,c2) in cache:
                return cache[r1,c1,r2,c2]
            if r1 == n or c1 == n or r2 == n or c2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")  
            elif r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]
            #elif r2 == n - 1 and c2 == n - 1:
            #    return grid[r2][c2]
            else:
                ans = grid[r1][c1]
                if r1 != r2 or c1 != c2:
                    ans += grid[r2][c2]
                a = dfs(r1 + 1, c1, r2 + 1, c2)
                b = dfs(r1 + 1, c1, r2, c2 + 1)
                c = dfs(r1, c1 + 1, r2 + 1, c2)
                d = dfs(r1, c1 + 1, r2, c2 + 1)
                ans += max(a,b,c,d)
                cache[r1,c1,r2,c2] = ans
                return ans
        return max(0, dfs(0,0,0,0))

