class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res = []
        def recursive(candidates, index, cur_list, target):
            if(target == 0):
                res.append( cur_list[:] )
                return
            for i in range(index,len(candidates)):
                if(candidates[i] > target):
                    break;
                cur_list.append(candidates[i])
                recursive(candidates, i, cur_list, target-candidates[i])
                cur_list.pop()
        recursive(candidates, 0, [], target)
        return res