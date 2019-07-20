class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(nums==None or len(nums)==0):
            return -1
        if(len(nums) == 1):
            return 0 if(nums[0]==target) else -1

        def findMin():
            begin = 0
            end = len(nums)-1
            if(nums[begin] < nums[end]):
                return begin
            while(begin <= end):
                mid = (begin+end)/2
                if(nums[mid] > nums[mid+1]):
                    return mid+1
                else:
                    if(nums[mid] < nums[begin]):
                        end = mid-1
                    else:
                        begin = mid+1
        
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

        min_num_pos = findMin()
        print "min->" + str(min_num_pos)
        if(nums[min_num_pos]==target):
            return min_num_pos
        if(min_num_pos == 0):
            return binary_search(0,len(nums)-1)
        if(target < nums[0]):
            return binary_search(min_num_pos,len(nums)-1)
        else:
            return binary_search(0,min_num_pos)