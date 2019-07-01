class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(nums==None or len(nums)==0):
            return -1
        if(len(nums)==1):
            if(nums[0]==target):
                return 0
            else:
                return -1
        def find_rotate_index(begin,end):
            if(nums[begin] < nums[end]):
                return 0
            while(begin <= end):
                pivot = (begin+end)/2
                if(nums[pivot]>nums[pivot+1]):
                    return pivot+1
                else:
                    if(nums[pivot]<nums[begin]):
                        end = pivot-1
                    else:
                        begin = pivot+1

        def binary_search(begin,end):
            while(begin <= end):
                mid = (begin+end)/2
                if(target < nums[mid]):
                    end = mid-1
                elif(target > nums[mid]):
                    begin = mid+1
                else:
                    return mid
            return -1
        
        index = find_rotate_index(0, len(nums)-1)
        if(nums[index] == target):
            return index
        if(index == 0):
            return binary_search(0,len(nums)-1)
        if(target < nums[0]):
            return binary_search(index,len(nums)-1)
        return binary_search(0,index)