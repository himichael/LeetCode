class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #del self.res[:]
        candidates = sorted(candidates)
        res = []
        self.dfs(candidates,target,0,[],res)
        return res
        
    def dfs(self, candidates, target, index, cur_list,res):
        if(0 == target):
            res.append( cur_list[:] )
            return
        size = len(candidates)
        for i in range(index,size):
            if(candidates[i] > target):
                break
            cur_list.append(candidates[i])
            self.dfs(candidates, target-candidates[i], i, cur_list,res)
            cur_list.pop()