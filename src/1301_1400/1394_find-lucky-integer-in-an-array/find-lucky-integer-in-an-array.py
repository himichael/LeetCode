class Solution(object):
    def findLucky(self, arr):
        d = dict()
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        keys = sorted(d.keys(),reverse=True)
        for k in keys:
            if d[k]==k:
                return k
        return -1