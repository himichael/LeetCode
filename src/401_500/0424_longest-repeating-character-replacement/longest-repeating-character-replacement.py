class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k<0:
            return 0
        left,right,res = 0,0,0
        d = dict()
        max_frequecy = 0
        while right<len(s):
            c = s[right]
            d[c] = d.get(c,0)+1
            max_frequecy = max(max_frequecy,d[c])
            if (right-left+1-max_frequecy)>k:
                d[s[left]] -=1
                left += 1
            res = max(res,right-left+1)
            right += 1
        return res