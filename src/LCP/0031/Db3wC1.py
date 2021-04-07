class Solution(object):
    def escapeMaze(self, maze):
        max_dep = len(maze)
        n = len(maze[0])
        m = len(maze[0][0])
        dirs = [(0,1), (1,0), (0,-1),(-1,0),(0,0)]
        s = set()
        def dfs(x, y, dep, magic_a, magic_b):
            if (x,y,dep,magic_a,magic_b) in s:
                return False
            s.add((x,y,dep,magic_a,magic_b))
            if x == n -1 and y == m - 1:
                return True
            if dep + 1 == max_dep:
                return False
            if n - 1 - x + m - 1 - y > max_dep - dep - 1:
                return False
            for i,j in dirs:
                xx,yy = x + i, y + j
                if 0 > xx or xx >= n or 0 > yy or yy >= m:
                    continue
                if maze[dep + 1][xx][yy] == '.':
                    if dfs(xx, yy, dep + 1, magic_a, magic_b):
                        return True
                else:
                    if not magic_a:
                        if dfs(xx, yy, dep + 1, True, magic_b):
                            return True
                    if not magic_b:
                        for next_dep in range(dep + 1, max_dep):
                            if dfs(xx, yy, next_dep, magic_a, True):
                                return True
            return False
        return dfs(0, 0, 0, False, False)