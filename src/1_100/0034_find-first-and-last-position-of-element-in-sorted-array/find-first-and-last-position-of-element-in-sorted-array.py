class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if(nums==0 or len(nums)==0):
            return [-1,-1]
        def findFirst():
            start = 0
            end = len(nums)-1
            while(start <= end):
                mid = (start+end)/2
                if(nums[mid]>target):
                    end = mid-1
                elif(nums[mid]<target):
                    start = mid+1
                else:
                    if(mid==0 or nums[mid-1]!=target):
                        return mid
                    else:
                        end = mid-1
            return -1
        
        def findLast():
            start = 0
            end = len(nums)-1
            while(start <= end):
                mid = (start+end)/2
                if(nums[mid] > target):
                    end = mid-1
                elif(nums[mid]<target):
                    start = mid+1
                else:
                    if(mid==len(nums)-1 or nums[mid+1]!=target):
                        return mid
                    else:
                        start = mid+1
            return -1
        return [findFirst(), findLast() ]