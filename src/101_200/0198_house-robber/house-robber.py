class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(nums==None or len(nums)==0):
            return 0
        #f(k) = max(f(k – 2) + A_kA k, f(k – 1))
        pre_max = 0
        cur_max = 0
        for i in nums:
            tmp = cur_max
            cur_max = max(pre_max+i,cur_max)
            pre_max = tmp
        return cur_max