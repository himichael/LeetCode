class Solution:
    def smallestRange(self, nums):
        n = len(nums)
        arr = []
        d = dict()
        for i in xrange(n):
            for j in xrange(len(nums[i])):
                arr.append( (nums[i][j],i) )
        arr = sorted(arr,key=lambda x:x[0])
        res = [float("-inf"),float("inf")]
        j = 0
        k = 0
        for i in xrange(len(arr)):
            if arr[i][1] not in d:
                d[arr[i][1]] = 1
                k += 1
            else:
                d[arr[i][1]] += 1
            if k==n:
                while d[arr[j][1]]>1:
                    d[arr[j][1]] -= 1 
                    j += 1
                if res[1]-res[0]>arr[i][0]-arr[j][0]:
                    res[1] = arr[i][0]
                    res[0] = arr[j][0]
        return res