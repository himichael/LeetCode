class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k<=0:
            return 0
        left = 0
        right = 0
        d = set(['a','e','i','o','u'])
        total = 0
        res = 0
        n = len(s)
        while right<k:
            if s[right] in d:
                total += 1
            right += 1
        res = max(res,total)
        while right<n:
            if s[left] in d:
                total -= 1
            if s[right] in d:
                total += 1
                res = max(res,total)
            right += 1
            left += 1
        return res