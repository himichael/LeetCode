class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def recursive(queue,stack):
            if(len(queue)==0):
                res.append(list(stack))
            size = len(queue)
            for i in range(size):
                stack.append(queue.pop(0))
                recursive(queue, stack)
                queue.append(stack.pop())
        recursive(nums, [])
        return res