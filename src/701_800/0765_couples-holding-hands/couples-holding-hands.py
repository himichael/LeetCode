class UnionFind(object):
    def __init__(self, n):
        self.roots = [i for i in range(n + 1)]

    def find(self, i):
        root = self.roots[i]
        while root != self.roots[root]:
            root = self.roots[root]
        while i != self.roots[i]:
            tmp = self.roots[i]
            self.roots[i] = root
            i = tmp
        return root
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        self.roots[root_q] = root_p

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        d = {}
        s = set()
        uf = UnionFind(n)
        for k, v in enumerate(row):
            d[v] = k // 2
        for i in range(0, n):
            uf.union(d[2 * i], d[2 * i + 1])
        for i in range(n):
            s.add(uf.find(i))
        return n - len(s)


    def minSwapsCouples(self, row):
        n = len(row) // 2
        d = {}
        s = set()
        uf = UnionFind(n)
        for k, v in enumerate(row):
            d[v] = k // 2
        for i in xrange(n):
            uf.union(d[2 * i], d[2 * i + 1])
        for i in xrange(n):
            s.add(uf.find(i))
        return n - len(s)