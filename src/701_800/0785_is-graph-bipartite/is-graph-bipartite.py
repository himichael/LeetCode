class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        self.valid = True

        def dfs(node, c):
            color[node] = c
            cNei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, cNei)
                    if not self.valid:
                        return
                elif color[neighbor] != cNei:
                    self.valid = False
                    return

        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not self.valid:
                    break
        
        return self.valid