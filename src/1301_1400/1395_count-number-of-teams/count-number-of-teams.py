class Solution(object):
    def numTeams(self, rating):
        n = len(rating)
        r = rating
        res = 0
        for i in xrange(0,n-2):
            for j in xrange(i+1,n-1):
                for k in xrange(j+1,n):
                    if r[i]<r[j]<r[k]:
                        res += 1
                    elif r[i]>r[j]>r[k]:
                        res += 1
        return res