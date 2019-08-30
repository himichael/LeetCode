class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if(not nums):
            return 
        nums.sort()



    #颜色分类的新实现方式
    def sortColors_2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if(not nums):
            return 
        zero = 0
        one = 0
        two = 0
        for i in nums:
            if( i==0 ):
                zero +=1
            elif( i==1 ):
                one += 1
            else:
                two += 1
        i = 0
        while( i<zero ):
            nums[i] = 0
            i += 1
        while( i<one+zero ):
            nums[i] = 1
            i += 1
        while( i<two+one+zero ):
            nums[i] = 2
            i += 1		



    #类似快速排序分割的方式
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if(not nums):
            return 
        i = 0
        j = 0
        n = len(nums)
        while( i<n ):
            if( nums[i]==0 ):
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
            i += 1
        i = j
        while( i<n ):
            if( nums[i]==1 ):
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
            i += 1
        #print nums
			