class Solution(object):
    def uniqueOccurrences(self, arr):
        if not arr:
            return True
        d1 = dict()
        for i in arr:
            d1[i] = d1.setdefault(i,0)+1
        s = set()
        for k in d1:
            s.add(d1[k])
        return len(s)==len(d1)


