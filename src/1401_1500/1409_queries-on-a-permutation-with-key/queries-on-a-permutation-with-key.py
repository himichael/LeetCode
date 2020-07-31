class Solution(object):
    def processQueries(self, queries, m):
        """
        :type queries: List[int]
        :type m: int
        :rtype: List[int]
        """
        p = [i for i in xrange(1,m+1)]
        q = queries
        res = []
        for i in q:
            k = 0
            while k<len(p):
                if i==p[k]:
                    res.append(k)
                    break
                k += 1
            val = p.pop(k)
            p.insert(0,val)
        return res

                        