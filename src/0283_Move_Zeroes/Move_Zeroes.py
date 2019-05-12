class Solution(object):
    def moveZeroes(self, arr):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index=0
        for i in range(len(arr)):
            if arr[i]!=0:
                tmp = arr[i]
                arr[i] = arr[index]
                arr[index] = tmp
                index+=1 