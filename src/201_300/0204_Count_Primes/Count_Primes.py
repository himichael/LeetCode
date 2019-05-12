class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        flags = []
        for i in range(n+1):
            flags.append(True)
        
        i = 2
        count = 0
        while i<n:
            if flags[i]:
                j = 2
                while (j*i)<n+1:
                    flags[j*i]= False
                    j += 1
                count += 1
            i += 1    
        
        return count