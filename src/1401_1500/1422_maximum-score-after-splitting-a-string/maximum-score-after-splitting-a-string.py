class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in xrange(1,n):
            a = 0
            b = 0
            for j in xrange(0,i):
                if s[j]=="0":
                    a += 1
            for k in xrange(i,n):
                if s[k]=="1":
                    b += 1
            res = max(res,a+b)
        return res
		
		
		
	# O(N)实现	
    def maxScore(self, s):
        n = len(s)
        res = 0
        cnt0 = 0
        cnt1 = 0
        for i in s:
            if i=="1":
                cnt1 += 1
        for i in xrange(n-1):
            if s[i]=="0":
                cnt0 += 1
            else:
                cnt1 -= 1
            res = max(res,cnt0+cnt1)
        return res