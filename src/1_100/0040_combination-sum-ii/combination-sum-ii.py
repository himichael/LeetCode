class Solution(object):
    def combinationSum2(self, candidates, target):
        if not candidates:
            return []
        res = []
        n = len(candidates)
        candidates = sorted(candidates)
        def dfs(index,arr,num):
            if num>target or index>n:
                return
            if num==target:
                res.append(arr)
                return
            if index<n and (candidates[index]>target or num+candidates[index]>target):
                return
            for i in xrange(index,n):
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                dfs(i+1,arr+[candidates[i]],num+candidates[i])
        dfs(0,[],0)
        return res