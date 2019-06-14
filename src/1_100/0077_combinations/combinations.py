class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        res = []
        
        def recursive(i,tmp):
            if(len(tmp)==k):
                res.append(list(tmp))
                return
            
            for j in range(i,n):
                tmp.append(arr[j])
                recursive(j+1,tmp)
                tmp.pop()
        recursive(0, [])
        return res