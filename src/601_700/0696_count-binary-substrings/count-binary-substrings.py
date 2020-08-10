class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        arr = []
        i = 0
        res = 0
        while i<n:
            c = s[i]
            count = 0
            while i<n and s[i]==c:
                i += 1
                count += 1
            arr.append(count)
        for i in xrange(1,len(arr)):
            res += min(arr[i],arr[i-1])
        return res