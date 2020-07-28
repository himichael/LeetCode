class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        if not target:
            return []
        s = set()
        for i in target:
            s.add(i)
        max_size = min(target[-1],n)
        res = []
        for i in xrange(1,max_size+1):
            if i not in s:
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
        return res